

from flask import Flask, render_template, request, session, jsonify

from DBConnection import Db
app = Flask(__name__)
app.secret_key="5555"
staticpath="C:\\Users\\ASUS\\Desktop\\final_project\\customer focused ecommerce site with ai bot\\static\\"

@app.route('/')
def login():
    return render_template('loginindex.html')

@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form['Name']
    password=request.form['Password']
    db = Db()
    qry="SELECT * FROM login WHERE username='"+ username +"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res!=None:
        session['lid']=res['lid']
        if res['type']=='admin':
            return '''<script>alert('Login Success');window.location='/admin_home'</script>'''
        elif res['type']=='user':
            return '''<script>alert('Login Success');window.location='/user_home'</script>'''
        else:
            return '''<script>alert('Invalid User');window.location='/'</script>'''
    else:
        return '''<script>alert('Invalid User');window.location='/'</script>'''


@app.route('/admin_home')
def hello_world():
    return render_template('admin/adminhome.html')


@app.route('/admin_add_brand')
def admin_add_brand():
    return render_template('admin/addbrand.html')
@app.route('/add_brand_post',methods=['post'])
def add_brand_post():
    brandname=request.form['textfield']
    qry="INSERT INTO `brand`(`brandname`)VALUES('"+brandname+"')"
    d=Db()
    d.insert(qry)

    return '''<script>  alert('brand added');  window.location='/admin_view_brand'</script>'''


@app.route('/admin_add_category')
def admin_add_category():
    return render_template('admin/addcategory.html')
@app.route('/add_category_post',methods=['post'])
def add_category_post():
    category=request.form['textfield']
    qry="INSERT INTO category(catname) VALUES('"+category+"')"
    d=Db()
    d.insert(qry)

    return  '''<script>  alert('category added');  window.location='/admin_view_category'</script>'''


@app.route('/admin_app_review')
def admin_app_review():
    return render_template('admin/appreview.html')


@app.route('/admin_edit_brand/<id>')
def admin_edit_brand(id):
    db = Db()
    qry = "select * from brand where brandid='" + str(id) + "'"
    res = db.selectOne(qry)
    return render_template('admin/editbrand.html', data=res)


@app.route('/edit_brand_post',methods=['post'])
def edit_brand_post():
    brandname=request.form['textfield']
    id = request.form['textfield2']
    db = Db()
    qry = "update brand set brandname='" + brandname + "' where  brandid='" + str(id) + "'"
    res = db.update(qry)
    return '''<script>alert('updated');window.location='/admin_view_brand'</script>'''

@app.route('/admin_edit_category/<id>')
def admin_edit_category(id):
    db=Db()
    qry="select * from category where caid='"+str(id)+"'"
    res=db.selectOne(qry)
    return render_template('admin/editcategory.html',data=res)


@app.route('/edit_category_post',methods=['post'])
def edit_category_post():
    category=request.form['textfield']
    id=request.form['textfield2']
    db=Db()
    qry="update category set catname='"+category+"' where  caid='"+str(id)+"'"
    res=db.update(qry)
    return '''<script>  alert('updated');  window.location='/admin_view_category'</script>'''



@app.route('/admin_feedback_view')
def admin_feeedback_view():
    db=Db()
    qry="SELECT feedback.*,registeruser.email,`registeruser`.`username`,`registeruser`.`email` FROM `feedback` INNER JOIN `registeruser` ON `feedback`.`userid`=`registeruser`.`userlogid` "
    res=db.select(qry)
    return render_template('admin/feedbackview.html',feedback=res)

@app.route('/admin_offer_add_or_modify/<b>')
def admin_offer_add_or_modify(b):
    session['prdtid']=b
    return render_template('admin/offeraddormodify.html')


@app.route('/offer_add_or_modify_post',methods=['post'])
def offer_add_or_modify_post():
    offer=request.form['textfield']
    x=session['prdtid']
    qry="INSERT INTO Offer(offeramount,`productid`) VALUES ('"+offer+"','"+str(x)+"')"
    d=Db()
    d.insert(qry)
    return '''<script>alert('offeradded');window.location='/admin_view_product'</script>'''

@app.route('/admin_offer_edit/<id>')
def admin_offer_edit(id):
    db=Db()
    qry="SELECT * FROM offer WHERE offerid='"+ id +"'"
    res=db.selectOne(qry)
    return render_template('admin/offeredit.html',data=res)

@app.route('/admin_offer_edit_post',methods=['post'])
def admin_offer_edit_post():
    offer=request.form['textfield']
    id=request.form['textfield2']
    db=Db()
    qry=" UPDATE offer SET offeramount='"+ offer + "' WHERE offerid='"+ str(id) +"'"
    res=db.update(qry)
    return '''<script>alert('offerupdated');window.location='/admin_view_product'</script>'''

@app.route('/admin_offer_delete/<id>')
def admin_offer_delete(id):
    db = Db()
    qry = "DELETE FROM `offer` WHERE `offerid`='" + id + "'"
    res = db.delete(qry)
    return '''<script>alert('offerdeleted');window.location='/admin_view_product'</script>'''





@app.route('/admin_offer_view/<id>')
def admin_offer_view(id):
    db=Db()
    session['oid']=id
    qry="SELECT product.productname,product.productimage,offer.offeramount,offer.offerid FROM offer INNER JOIN product ON offer.productid=product.productid WHERE product.productid='"+str(id)+"'"
    res=db.select(qry)
    return render_template('admin/offerview.html',i=res)

@app.route('/admin_password_change_post',methods=['post'])
def admin_password_change():
    currentpassword=request.form['textfield']
    newpassword=request.form['textfield2']
    confirmpassword=request.form['textfield3']
    db=Db()
    qry="select * from login where password='"+ currentpassword +"'"
    res = db.selectOne(qry)
    if res!=None:
        if confirmpassword==newpassword:
            qry = "update login set password='"+newpassword+"' where lid = '"+str(session['lid'])+"'"
            res = db.update(qry)
            return '''<script>alert('password updated');window.location='/'</script>'''

        else:
            return '''<script>alert('invalid');window.location='/password_change'</script>'''

    else:
        return '''<script>alert('invalid ');window.location='/password_change'</script>'''



@app.route('/password_change')
def password_change():
    return render_template('admin/passwordchange.html')

@app.route('/admin_offer_view_post',methods=['post'])
def offer_view_post():
    productid=request.form['textfield']
    return "ok"

@app.route('/admin_producr_history_order_sud/<id>')
def admin_producr_history_order_sud(id):
    db=Db()
    qry="SELECT ordersub.*,product.`productname`,product.price,product.productcolor,product.productdescription,product.productimage FROM product INNER JOIN ordersub ON ordersub.productid=product.productid where ordersub.omid='"+id+"'"
    res=db.select(qry)
    return render_template('admin/producrhistoryordersud.html',data=res)


@app.route('/admin_product_add')
def admin_product_add():
    qry="select * from category"
    d=Db()
    cat=d.select(qry)
    qry="select * from brand"
    d=Db()
    br=d.select(qry)
    return render_template('admin/productadd.html',cate=cat,bran=br)
@app.route('/product_add_post',methods=['post'])
def product_add_post():

    productname=request.form['textfield2']
    productprice=request.form['textfield3']
    productdescription=request.form['textfield4']
    productcategory=request.form['select']
    brand=request.form['select2']
    productimage=request.files['fileField']
    productimage.save(staticpath+"product\\"+productimage.filename)
    url="/static/product/"+productimage.filename
    productsize=request.form['select3']
    productcolor=request.form['select4']
    qry="INSERT INTO PRODUCT(productname,caid,brandid,price,productsize,productcolor,productdescription,productimage) VALUES('"+productname+"','"+productcategory+"','"+brand+"','"+productprice+"','"+productsize+"','"+productcolor+"','"+productdescription+"','"+url+"')"
    d=Db()
    d.insert(qry)
    return '''<script>alert('productadded');window.location='/admin_view_product'</script>'''


@app.route('/admin_edit_product/<id>')
def admin_product_edit(id):
    db = Db()
    session['pid']=id
    qry = "select * from product where productid='" + str(id) + "'"
    res = db.selectOne(qry)
    qry1 = "select * from brand"
    res1=db.select(qry1)
    qry2 = "select * from category"
    res2 = db.select(qry2)
    return render_template('admin/productedit.html', data=res,dat=res1,da=res2)


@app.route('/edit_product_post', methods=['post'])
def edit_product_post():
   productname = request.form['textfield2']
   pid = session['pid']
   productprice = request.form['textfield3']
   productdescription = request.form['textfield4']
   productcategory = request.form['select']
   brand = request.form['select2']
   productsize = request.form['select3']
   productcolor = request.form['select4']

   if  'fileField' in request.files  :
       productimage = request.files['fileField']

       if productimage.filename!='':
           productimage.save( staticpath+"product\\" + productimage.filename)
           url = "/static/product/" + productimage.filename

           db = Db()
           qry = "UPDATE product SET productname='" + productname +"',caid='" + productcategory + "',brandid='" + brand + "',price='" +productprice+ "',productsize='" +productsize+ "',productcolor='" +productcolor+ " ',productdescription='" +productdescription+ "',productimage='" +url+ "'   WHERE productid='" +str(pid)+ "'"
           #qry = "UPDATE product SET productname='" + productname +"', price='"+productprice+"' WHERE productid='" +str(id)+ "'"
           res = db.update(qry)
           return '''<script>alert('updated');window.location='/admin_view_product'</script>'''
       else:
           db = Db()
           qry = "UPDATE product SET productname='" + productname + "',caid='" + productcategory + "',brandid='" + brand + "',price='" + productprice + "',productsize='" + productsize + "',productcolor='" + productcolor + " ',productdescription='" + productdescription + "'  WHERE productid='" + str(
               pid) + "'"
           # qry = "UPDATE product SET productname='" + productname +"', price='"+productprice+"' WHERE productid='" +str(id)+ "'"
           res = db.update(qry)
           return '''<script>alert('updated');window.location='/admin_view_product'</script>'''

   else:
       db = Db()
       qry = "UPDATE product SET productname='" + productname + "',caid='" + productcategory + "',brandid='" + brand + "',price='" + productprice + "',productsize='" + productsize + "',productcolor='" + productcolor + " ',productdescription='" + productdescription + "'  WHERE productid='" + str(
           pid) + "'"
       # qry = "UPDATE product SET productname='" + productname +"', price='"+productprice+"' WHERE productid='" +str(id)+ "'"
       res = db.update(qry)
       return '''<script>alert('updated');window.location='/admin_view_product'</script>'''


# @app.route('/admin_product_list_sales_igure')
# def admin_product_list_sales_igure():
#     return render_template('admin/productlistsalesigure.html')
# @app.route('/product_list_sales_igure_post',methods=['post'])
# def product_list_sales_igure_post():
#     datefrom=request.form['textfield']
#     dateto=request.form['textfield2']
#     return "ok"


@app.route('/admin_product_rate_and_review/<pid>')
def admin_product_rate_and_review(pid):
    q = "select registeruser.username,registeruser.image,productrateandreview.* from registeruser inner join productrateandreview on registeruser.userlogid=productrateandreview.userid where productrateandreview.pid='" + pid + "'"
    d = Db()
    res = d.select(q)
    return render_template('admin/productrateandreview.html',data=res)

@app.route('/admin_purchase_history_order_main')
def admin_purchase_history_order_main():
    db=Db()
    qry="SELECT `ordermain`.*, `registeruser`.`username`, `registeruser`.`email`,`registeruser`.`phone` FROM `registeruser` INNER JOIN `ordermain` ON `ordermain`.`userid`=`registeruser`.`userlogid`"
    res=db.select(qry)
    return render_template('admin/purchasehistoryordermain.html',data=res)



@app.route('/purchase_history_order_main_post',methods=['post'])
def purchase_history_order_main_post():

    fromdate=request.form['textfield']
    todate=request.form['textfield2']
    db=Db()
    qry = "SELECT `ordermain`.*, `registeruser`.`username`, `registeruser`.`email`,`registeruser`.`phone` FROM `registeruser` INNER JOIN `ordermain` ON `ordermain`.`userid`=`registeruser`.`userlogid` where ordermain.date between '"+fromdate+"' and '"+todate+"'"
    res = db.select(qry)
    return render_template('admin/purchasehistoryordermain.html', data=res)


@app.route('/admin_registered_customer1')
def admin_registered_customer1():
    qry="SELECT * FROM `registeruser`"
    d=Db()
    res=d.select(qry)
    return render_template('admin/registeredcustomer1.html',user=res)

@app.route('/admin_respond_to_feedback/<id>')
def admin_respond_to_feedback(id):
    db=Db()
    qry="SELECT * FROM feedback WHERE fid='"+id+"'"
    res=db.selectOne(qry)
    return render_template('admin/respondtofeedback.html',data=res)

@app.route('/respond_to_feedback_post',methods=['post'])
def respond_to_feedback_post():
    f_id = request.form['fd_id']
    respond=request.form['textfield']
    db = Db()
    qry = "update feedback set respond='"+ respond +"', status='responded' where fid='"+f_id+"'"
    print(qry)
    res=db.update(qry)
    return '''<script>alert('response added');window.location='/admin_feedback_view'</script>'''



@app.route('/admin_view_brand')
def admin_view_brand():
    qry="select * from brand"
    d=Db()
    res=d.select(qry)
    return render_template('admin/viewbrand.html',data=res)

@app.route('/view_brand_post',methods=['post'])
def view_brand_post():
    brandname=request.form['textfield']
    db = Db()
    qry = "select * from brand where brandname like '%"+brandname+"%'"
    res = db.select(qry)
    return render_template('admin/viewbrand.html',data=res)


@app.route('/admin_delete_brand/<id>')
def admin_delete_brand(id):
    db=Db()
    qry="DELETE FROM `brand` WHERE `brandid`='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert('deleted');window.location='/admin_view_brand'</script>'''


@app.route('/admin_view_category')
def admin_view_category():
    qry="select * from category"
    d=Db()
    res=d.select(qry)
    return render_template('admin/viewcategory.html',data=res)

@app.route('/admin_delete_category/<id>')
def admin_delete_category(id):
    db=Db()
    qry="DELETE FROM category WHERE caid='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert('deleted');window.location='/admin_view_category'</script>'''


@app.route('/admin_view_product')
def admin_view_product():
    qry="SELECT product.*,category.catname,brand.brandname FROM product INNER JOIN category ON product.caid=category.caid INNER JOIN brand ON brand.brandid=product.brandid"
    d=Db()
    res=d.select(qry)
    return render_template('admin/viewproduct.html',data=res)
@app.route('/view_product_post',methods=['post'])
def view_product_post():
    productname=request.form['textfield']
    db = Db()
    qry = "SELECT product.*,category.catname,brand.brandname FROM product INNER JOIN category ON product.caid=category.caid INNER JOIN brand ON brand.brandid=product.brandid WHERE `product`.`productname` LIKE '%"+productname+"%'"
    res = db.select(qry)
    return render_template('admin/viewproduct.html', data=res)

@app.route('/admin_delete_product/<id>')
def admin_delete_product(id):
    db = Db()
    qry = "DELETE FROM `product` WHERE `productid`='" + id + "'"
    res = db.delete(qry)
    return '''<script>alert('productdeleted');window.location='/admin_view_product'</script>'''


        #completed admin module


@app.route('/user_user_registration')
def user_user_registration():
    return render_template('user/userregistration.html')
@app.route('/user_registration_post',methods=['post'])
def user_registration_post():

    photo=request.files['file']
    photo.save(staticpath+"user\\" + photo.filename)
    url = "/static/user/" + photo.filename
    name=request.form['textfield']
    gender=request.form['radio']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    place=request.form['place']
    post=request.form['post']
    district = request.form['textfield6']
    pin=request.form['textfield4']
    state=request.form['textfield5']
    password=request.form['textfield7']
    confirmpassword=request.form['textfield8']
    db=Db()
    if password == confirmpassword:
        qry="INSERT INTO login(username,password,type) VALUES('"+ email +"','"+ password +"','user')"
        res=db.insert(qry)
        qry1="INSERT INTO registeruser(username,email,phone,place,post,gender,district,state,pin,userlogid,image) VALUES('"+ name +"','"+ email +"','"+ phone +"','"+ place +"','"+ post +"','"+ gender +"','"+ district +"','"+ state +"','"+ pin +"','"+ str(res) +"','"+ url +"')"
        res1=db.insert(qry1)
        return '''<script>alert('registration success');window.location='/'</script>'''
    else:
        return '''<script>alert('Invalid!!');window.location='/user_user_registration'</script>'''




@app.route('/user_home')
def user_home():
    # return render_template('user/userhome.html')
    return render_template('user/maintemp.html')



@app.route('/user_user_profile')
def user_user_profile():
    qry="SELECT * FROM registeruser WHERE userlogid='"+ str(session['lid'])+"'"
    db=Db()
    res=db.selectOne(qry)
    print(res)
    return render_template('user/userprofile.html',data=res)

@app.route('/user_user_account_modify/<id>')
def user_user_account_modify(id):
    db = Db()
    qry = "SELECT * FROM registeruser WHERE `userlogid`='"+id+"'"
    res = db.selectOne(qry)
    return render_template('user/useraccountmodify.html', data=res)

@app.route('/user_account_modify_post',methods=['post'])
def user_account_modify_post():
    uid = request.form['id']
    name = request.form['textfield']
    gender = request.form['radio']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    place = request.form['place']
    post = request.form['post']
    district = request.form['textfield6']
    pin = request.form['textfield4']
    state = request.form['textfield5']
    db = Db()
    if 'file' in request.files:
        photo = request.files['file']
        if photo.filename!="":
            photo.save(staticpath+"user\\" + photo.filename)
            url = "/static/user/" + photo.filename
            qry = "UPDATE registeruser SET username='"+ name +"',email='"+ email +"',phone='"+ phone +"',place='"+ place +"',post='"+ post +"',gender='"+ gender+"',district='"+ district +"',state='"+ state +"',pin='"+ pin +"',image='"+ url +"' WHERE userlogid='"+ uid +"'"
            res = db.update(qry)
            return '''<script>alert('user details updated');window.location='/user_user_profile'</script>'''
        else:
            qry = "UPDATE registeruser SET username='" + name + "',email='" + email + "',phone='" + phone + "',place='" + place + "',post='" + post + "',gender='" + gender + "',district='" + district + "',state='" + state + "',pin='" + pin + "' WHERE userlogid='" + uid + "'"
            res = db.update(qry)
            return '''<script>alert('user details updated');window.location='/user_user_profile'</script>'''
    else:
        qry = "UPDATE registeruser SET username='" + name + "',email='" + email + "',phone='" + phone + "',place='" + place + "',post='" + post + "',gender='" + gender + "',district='" + district + "',state='" + state + "',pin='" + pin + "' WHERE userlogid='" + uid + "'"
        res = db.update(qry)
        return '''<script>alert('user details updated');window.location='/user_user_profile'</script>'''


@app.route('/user_password_change')
def user_password_change():
    return render_template('user/passwordchange.html')

@app.route('/user_password_change_post', methods=['post'])
def user_password_change_post():
    cp = request.form['textfield']
    np = request.form['textfield2']
    cnp = request.form['textfield3']
    db = Db()
    qry = "select * from login where password='" + cp + "'"
    res = db.selectOne(qry)
    if res != None:
        if cp == np:
            qry = "update login set password='" + cnp+ "' where lid = '" + str(session['lid']) + "'"
            res = db.update(qry)
            return '''<script>alert('password updated');window.location='/'</script>'''

        else:
            return '''<script>alert('invalid');window.location='/password_change'</script>'''

    else:
        return '''<script>alert('invalid ');window.location='/password_change'</script>'''


@app.route('/user_product_view')
def user_product_view():
    db=Db()
    qry="SELECT product.*,category.catname,brand.brandname FROM product INNER JOIN category ON product.caid=category.caid INNER JOIN brand ON brand.brandid=product.brandid"
    res=db.select(qry)
    # qry1="SELECT offeramount FROM offer WHERE productid=''"
    #  res1=db.selectOne(qry1)
    return render_template('user/productview.html',data=res)

@app.route('/user_addto_product_cart/<prod_id>')
def user_addto_product_cart(prod_id):

    return render_template('user/add_to_cart.html',pid=prod_id)
@app.route('/user_addtocart',methods=["post"])
def user_addtocart():
    pid=request.form["pid"]
    qty=request.form["textfield2"]
    db = Db()
    qry = "insert into cart(productid,userid,qty) values('"+pid+"','"+str(session["lid"])+"','"+qty+"')"
    res = db.insert(qry)
    return '''<script>alert("added to cart");window.location='/user_product_view'</script>'''
@app.route('/user_view_cart_product')
def user_view_cart_product():
    q="select cart.*,product.* from cart inner join product on cart.productid=product.productid where cart.userid='"+str(session["lid"])+"'"
    d=Db()
    res=d.select(q)
    total=0
    for i in res:
        q1="select offeramount from offer where productid='"+str(i["productid"])+"'"
        r=d.selectOne(q1)
        if r is not None:
            total=(total+(int(i["qty"]*i["price"])))-r["offeramount"]
        else:
            total = (total + (int(i["qty"] * i["price"])))


    return render_template('user/productcart.html',data=res,total=total)


@app.route('/user_delete_cart/<cartid>')
def user_delete_cart(cartid):
    q="delete from cart where cartid='"+cartid+"'"
    d=Db()
    res=d.delete(q)
    return '''<script>alert("cart Deleted");window.location='/user_view_cart_product'</script>'''

@app.route('/user_addto_product_wishlist/<prod_id>')
def user_addto_product_wishlist(prod_id):
    db=Db()
    qry="INSERT INTO wishlist(productid,userid) VALUES('"+ prod_id+"','"+ str(session['lid']) +"')"
    res=db.insert(qry)
    return '''<script>alert("added to wishlist");window.location='/user_product_view'</script>'''


@app.route('/user_product_wishlist')
def user_product_wishlist():
    q="select wishlist.*,product.* from wishlist inner join product on wishlist.productid=product.productid where wishlist.userid='"+str(session["lid"])+"'"
    d=Db()
    res=d.select(q)
    return render_template('user/productwishlist.html',data=res)
@app.route('/user_product_wishlistremove/<wid>')
def user_product_wishlistremove(wid):
    q="delete from wishlist where wlid='"+wid+"'"
    d=Db()
    res=d.delete(q)
    return '''<script>alert("deleted from your wishlist");window.location='/user_product_wishlist'</script>'''

@app.route('/user_purcahse_product/<total>')
def user_purcahse_product(total):
    return render_template('user/purchase_product.html',tot=total)
@app.route('/user_buy_product',methods=["post"])
def user_buy_product():
    amount=request.form["total"]
    bank=request.form["bank"]
    pin=request.form["textfield2"]
    q="select productid,qty from cart where userid='"+str(session["lid"])+"'"
    d=Db()
    res=d.select(q)
    if len(res)>0:
        bank_check="select amount from bank where bank='"+bank+"' and pin='"+pin+"'"
        bres=d.selectOne(bank_check)
        if int(bres["amount"])>int(amount):

            omain="insert into ordermain(userid,date,totalamount)values('"+str(session["lid"])+"',curdate(),'"+amount+"')"
            ordermainid=d.insert(omain)
            for i in res:
                pr="select price from product where productid='"+str(i["productid"])+"'"
                r=d.selectOne(pr)
                if r is not None:
                    singleamount=int(r["price"]*i["qty"])
                    osub="insert into ordersub(omid,`count`,amount,productid)values('"+str(ordermainid)+"','"+str(i["qty"])+"','"+str(singleamount)+"','"+str(i["productid"])+"')"
                    d.insert(osub)
                else:
                    return "error"
            bankqry="UPDATE bank set amount=amount-'"+amount+"' where bank='"+bank+"' and pin='"+pin+"'"
            d.update(bankqry)

            payment="INSERT INTO payment(omid,amount,date)value('"+str(ordermainid)+"','"+amount+"',curdate())"
            d.insert(payment)

            cartdele="delete from cart where userid='"+str(session["lid"])+"'"
            d.delete(cartdele)
            return '''<script>alert("Purchase completed");window.location='/user_product_view'</script>'''

        else:
            return '''<script>alert("BALANCE LOW");window.location='/user_view_cart_product'</script>'''
    else:
        return '''<script>alert("NO DATA");window.location='/user_view_cart_product'</script>'''

@app.route('/user_product_rate/<pid>')
def user_product_rate(pid):
    q="select registeruser.username,registeruser.image,productrateandreview.* from registeruser inner join productrateandreview on registeruser.userlogid=productrateandreview.userid where productrateandreview.pid='"+pid+"'"
    d=Db()
    res=d.select(q)
    return render_template('user/product_rate_review.html',pid=pid,data=res)
@app.route('/user_send_rtings',methods=["post"])
def user_send_rtings():
    pid=request.form["pid"]
    rate=request.form["rate"]
    review=request.form["textarea"]
    q="insert into productrateandreview(preview,prate,userid,date,pid)value('"+review+"','"+rate+"','"+str(session["lid"])+"',curdate(),'"+pid+"')"
    d=Db()
    d.insert(q)
    return user_product_rate(pid)
@app.route('/user_site_feedback')
def user_site_feedback():

    return render_template('user/feedbackadd.html')
@app.route('/site_feedback_post',methods=['post'])
def site_feedback_post():
    feedbac = request.form["textarea"]
    q = "insert into feedback(feedback,userid,date,respond,status)value('" + feedbac + "','" + str(
        session["lid"]) + "',curdate(),'pending','pending')"
    d = Db()
    d.insert(q)
    return '''<script>alert("Send");window.location='/user_site_feedback'</script>'''
@app.route('/user_view_feedback')
def user_view_feedback():
    q="select * from feedback where userid='"+str(session["lid"])+"'"
    d=Db()
    res=d.select(q)
    return render_template('user/view_feedback_reply.html',data=res)
@app.route('/user_purchase_history')
def user_purchase_history():
    q="select * from ordermain where userid='"+str(session["lid"])+"' order by omid desc"
    d=Db()
    res=d.select(q)
    return render_template('user/purchasehistoryordermain.html',data=res)
@app.route('/user_purchase_history_post',methods=["post"])
def user_purchase_history_post():
    fd=request.form["d1"]
    td=request.form["d2"]
    q="select * from ordermain where userid='"+str(session["lid"])+"' and date between '"+fd+"' and '"+td+"'"
    d=Db()
    res=d.select(q)
    return render_template('user/purchasehistoryordermain.html',data=res)

@app.route('/user_producr_history_order_sud/<id>')
def user_producr_history_order_sud(id):
    db=Db()
    qry="SELECT ordersub.*,product.`productname`,product.price,product.productcolor,product.productdescription,product.productimage FROM product INNER JOIN ordersub ON ordersub.productid=product.productid where ordersub.omid='"+id+"'"
    res=db.select(qry)
    return render_template('user/producrhistoryordersud.html',data=res)
@app.route('/userchatbot')
def userchatbot():
    return render_template('user/Bot.html')
#___________________________________andchatbotttttt



import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
# f=open('chatbot.txt','r',errors = 'ignore')
f=open('C:\\Users\\ASUS\\Desktop\\final_project\\customer focused ecommerce site with ai bot\\static\\chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase


sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words



lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey","hlo","A")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    print("---",sent_tokens)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        print("loading response")
        return robo_response

@app.route('/and_chatbot',methods=['post'])
def and_chatbot():
    question=request.form['msg']
    user_response=question.lower()
    if(greeting(user_response)!=None):
            print("oooooooooooooooooooooooooooooooooooooooooo")
            # print("ROBO: "+greeting(user_response))
            # k = {}
            # k['status'] = 'ok'
            # k['data'] = greeting(user_response)

            # return demjson.encode(k)
            return jsonify(status="ok",data=greeting(user_response))

    else:
        # print("ROBO: ",end+"")
        strr=response(user_response)
        print("rrrr")
        print(strr)
        sent_tokens.remove(user_response)
        k1=strr.split('\n')
        aa=k1[len(k1)-1]


        # return demjson.encode(k)
        return jsonify(status="ok", data=strr)
if __name__ == '__main__':
    app.run(debug=True)
