    // Giảm giá trị của số lượng sản phẩm của order trong giỏ hàng
    function decrement(id){
        var id_quantity = 'quantity-product-cart-' + id;
        var id_price = 'price-product-cart-' + id;
        var id_total_price = 'total-price-cart-' + id;
        var delete_order = 'delete-' + id;
    
        var quantity = parseInt(document.getElementById(id_quantity).value);
        if(quantity -1 !=0){
    
            document.getElementById(id_quantity).value = quantity - 1; 
            var total_price  = (quantity-1) * parseInt(document.getElementById(id_price).textContent.trim().slice(0,-2).replaceAll(',',''));
            document.getElementById(id_total_price).innerHTML = total_price.toLocaleString() + ' đ';
    
    
            var total_price_all_cart = 0;
            var element_check_order = document.getElementsByName('checkbox_products[]');
            var total_price_of_each_order = document.getElementsByClassName('total-price-cart'); 
            for(var i =0; i<element_check_order.length; i++){
                if(element_check_order[i].checked === true){
                    total_price_all_cart += parseInt( total_price_of_each_order[i].textContent.trim().slice(0,-2).replaceAll(',', ''));
                }
            }
            document.getElementById('temp_total_price').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
            document.getElementById('total_price_official').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
    
        }   
        // nếu giá trị số lượng về 0 folow link xóa sản phẩm khỏi giỏ hàng
        else {
            if (confirm('Are you want to remove this order from your cart?'))
            {   
                var url = document.getElementById(delete_order).getAttribute("href");
                console.log(url);
                window.location.href = url;
            }
            else
            {
                event.stopPropagation(); event.preventDefault();
            };
        }
    }
    
    // Tăng giá trị của số lượng sản phẩm của order trong giỏ hàng
    function increase(id){
        var id_quantity = 'quantity-product-cart-' + id;
        var id_price = 'price-product-cart-' + id;
        var id_total_price = 'total-price-cart-' + id;
        var quantity = parseInt(document.getElementById(id_quantity).value);
        document.getElementById(id_quantity).value = quantity + 1;
        var total_price = (quantity + 1) * parseInt(document.getElementById(id_price).textContent.slice(0,-2).replaceAll(',',''));
        document.getElementById(id_total_price).innerHTML = total_price.toLocaleString() + ' đ';
    
    
    
        var total_price_all_cart = 0;
        var element_check_order = document.getElementsByName('checkbox_products[]');
        var total_price_of_each_order = document.getElementsByClassName('total-price-cart'); 
        for(var i =0; i<element_check_order.length; i++){
            if(element_check_order[i].checked === true){
                total_price_all_cart += parseInt( total_price_of_each_order[i].textContent.trim().slice(0,-2).replaceAll(',', ''));
            }
        }
        document.getElementById('temp_total_price').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
        document.getElementById('total_price_official').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
    
    }
    
    // Tạo thứ tự cho danh sách sản phẩm trong mục quản lý sản phẩm
    
    
    // đánh dấu tất cả check box và loại bỏ tất cả các check box và thay đổi giá trị liên quan
    function checkbox_order_cart_for_all(){
        var order_count = 0;
        var total_price_all_cart = 0;
        var element_check_order = document.getElementsByName('checkbox_products[]');
        var total_price_of_each_order = document.getElementsByClassName('total-price-cart'); 
        if(document.getElementById('all_checkbox').checked === true){
            for(var i=0; i<element_check_order.length; i++){
                order_count +=1;
                element_check_order[i].checked = true;
                total_price_all_cart += parseInt( total_price_of_each_order[i].textContent.trim().slice(0,-2).replaceAll(',', ''));
            }
            if(order_count!=0){
                document.getElementById('buy').disabled = false;
            }
            
        }
        if(document.getElementById('all_checkbox').checked === false){
            for(var i =0; i<element_check_order.length; i++){
                element_check_order[i].checked = false;
                document.getElementById('buy').disabled = true;
            }
        }
        document.getElementById('buy').value = 'Buy(' + order_count + ')';
        document.getElementById('temp_total_price').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
        document.getElementById('total_price_official').innerHTML = total_price_all_cart.toLocaleString() + ' đ';
    }
    
    
    // đánh dấu từng check box và thay đổi các giá trị liên quan   
    function check_order_cart(){
        var order_count = 0;
        var total_price_all_cart = 0;
        var element_check_order = document.getElementsByName('checkbox_products[]'); // lấy danh sách các check box
        var total_price_of_each_order = document.getElementsByClassName('total-price-cart'); // lấy danh sách các giá trị ở ô total price của từng order 
        var flag = false;
        for(var i =0; i<element_check_order.length; i++){
            if(element_check_order[i].checked === false){
                document.getElementById('all_checkbox').checked = false; // ô check box all
                flag = true;
            }
            else {
                order_count +=1;
                total_price_all_cart += parseInt( total_price_of_each_order[i].textContent.trim().slice(0,-2).replaceAll(',', ''));
            }
        }
        if(flag===false){
            document.getElementById('all_checkbox').checked = true;
        }
        buy_button = document.getElementById('buy');
        buy_button.value = 'Buy(' + order_count + ')';
        document.getElementById('temp_total_price').innerHTML = total_price_all_cart.toLocaleString() + ' đ'; // giá trị tạm tính
        document.getElementById('total_price_official').innerHTML = total_price_all_cart.toLocaleString() + ' đ'; // tổng giá trị

        if(order_count==0){

            buy_button.disabled = true;
        }
        else{

            buy_button.disabled = false;
        }
    }
    
    
    function generation_sn_for_product(){
        var sn = document.getElementsByClassName('sn1');
        for(var i=0; i<sn.length; i++){
            sn[i].innerHTML = i + 1;
        }
        var sn = document.getElementsByClassName('sn2');
        for(var i=0; i<sn.length; i++){
            sn[i].innerHTML = i + 1;
        }
    }
    generation_sn_for_product();
    
    // Tăng giảm sóo lượng sản phẩm ở phần đặt hàng dùng jquery
    
    $(document).ready(function(){
        // Animation for out messages
        $(".btn-custom").click(function(){
            $("#alert").fadeOut("slow");
        });

        //decrement quantity of product for order  
        $("#decrement-quantity").click(function(){
            var quantity = parseInt($("#quantity").val());
            if(quantity<=0){
                $("#quantity").val(0);
            }
            else{
                $("#quantity").val(quantity - 1);
            }
        });

        //increase quantity of product for order  
        $("#increase-quantity").click(function(){
            var quantity = parseInt($("#quantity").val());
            $("#quantity").val(quantity + 1);
        });

        // Acount toogle
        $('#toogle-account').hide();
        $('#account').click(function(){
            $('#toogle-account').toggle(100);
        });

        // Check order in cart for buy button and checkout form
        $('#buy').attr('disabled','disabled');

        $('#checkout-form').hide(100);
        $('#buy').click(function(){
            $('#cart-form').css("opacity", "0.4");
            $('#checkout-form').show(100);
        });

        $('#cancel-checkout').click(function(){
            $('#checkout-form').hide(100);
            $('#cart-form').css("opacity", "1");
        });
        // Menu manage
        $('.position-menu-extend').hide();
        $('.position-extend-button').click(function(){
            $('.position-menu-mini').hide();
            $('.position-menu-extend').show(100);
            $('.manage-page').css("opacity", "0.7")
        });

        $('.position-close-button').click(function(){
            $('.position-menu-mini').show();
            $('.position-menu-extend').hide();
            $('.manage-page').css("opacity", "1")
        })

        $('.manage-products-menu').click(function(){
            $('.manage-products').show();
            $('.manage-checkouts').hide();
            $('.manage-products-menu').addClass('bg-info');
            $('.manage-checkouts-menu').removeClass('bg-info');
        });

        $('.manage-checkouts-menu').click(function(){
            $('.manage-checkouts').show();
            $('.manage-products').hide();
            $('.manage-checkouts-menu').addClass('bg-info');
            $('.manage-products-menu').removeClass('bg-info');
        });
    });