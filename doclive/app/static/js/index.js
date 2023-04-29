function displayMessage(data){
    $('.loader').css('display','none')
    $("#message-body").remove();
    $('#django-message').append('<div class="container" id="message-body"><div class="alert alert-dismissible fade show" role="alert"><a></a><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div></div>');
    mainDiv = document.getElementById('message-body'),
    childDiv = mainDiv.getElementsByTagName('div')[0]
    childDiv.classList.add('alert-'+data.status);
    childDiv.getElementsByTagName('a')[0].text = data.message
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function validatePassword(){
    var pw = document.getElementById("password").value;
    var Rpw = document.getElementById("re_password").value;
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var username = document.getElementById("username").value;
    var gender = document.getElementById("gender").value;
    var email = document.getElementById("email").value;
    var messageData = new Object();

    if (!pw||!firstName||!lastName||!username||!gender||!email) {
        messageData.message = "Please Fill all the details";
        messageData.status = "danger";
        displayMessage(messageData)
        return false;
    }

    if (!Rpw){
        messageData.message = "Please Fill all the details";
        messageData.status = "danger";
        displayMessage(messageData)
        return false;
    }

    if (pw !=Rpw){
        messageData.message = "**Both the Password must be same";
        messageData.status = "danger";
        displayMessage(messageData)
        return false;
    }
    if (pw.length < 8){
        messageData.message = "**Password length must be atleast 8 characters"
        messageData.status = "danger";
        displayMessage(messageData)
        return false;
    }
    $("#message-body").remove();

}

function registration(){
$('.loader').css('display','block')
    var fileFormData = new FormData();
    var messageData = new Object();
    messageData.status = "danger";

    if (validatePassword()==false){
        return;
    }

    var firstName = $('#firstName').val().trim();
    var lastName = document.getElementById("lastName").value;
    var username = document.getElementById("username").value;
    var phone = document.getElementById("phone").value
    var gender = document.getElementById("gender").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var re_password = document.getElementById("re_password").value;

    if (validatePassword()==false){
        return;
    }

    fileFormData.append('first_name',firstName);
    fileFormData.append('last_name',lastName);
    fileFormData.append('username',username);
    fileFormData.append('phone_number',phone);
    fileFormData.append('gender',gender);
    fileFormData.append('email',email);
    fileFormData.append('password',password);
    fileFormData.append('re_password',re_password);

    console.log(fileFormData)
    $.ajax({
          type: 'POST',
          url:'/user/v1/user-register/',
          headers:{
          'contentType': 'application/json',
          },
          contentType: false, //this is requireded please see answers above
          processData: false,
          data:fileFormData,
          success: function(data){
          $('.loader').css('display','none')
            console.log(data)
            if (data.status==200){
                location.href ='/login'
                messageData.message = data.message;
                messageData.status = "info";
                displayMessage(messageData)
            }
            else{
                messageData.message = data.message;
                messageData.status = "danger";
                displayMessage(messageData)
            }
          },
          error: function(data){
          $('.loader').css('display','none')
           console.log(data)
            messageData.message = data.message;
            messageData.status = "danger";
            displayMessage(messageData)

          },
      });
}


function login(){
$('.loader').css('display','block')
    var fileFormData = new FormData();
    var messageData = new Object();
    messageData.status = "danger";

    var username = $('#username').val().trim();
    var password = document.getElementById("password").value;

    fileFormData.append('username',username);
    fileFormData.append('password',password);

    console.log(fileFormData)
    $.ajax({
          type: 'POST',
          url:'/user/v1/login/',
          headers:{
          'contentType': 'application/json',
          },
          contentType: false, //this is requireded please see answers above
          processData: false,
          data:fileFormData,
          success: function(data){
          $('.loader').css('display','none')
            console.log(data)
            if (data.status==200){
                console.log('Login Success')
                location.href ='/dashboard'
            }
            else{
                messageData.message = data.message;
                messageData.status = "danger";
                displayMessage(messageData)
            }
          },
          error: function(data){
          $('.loader').css('display','none')
           console.log(data)
            messageData.message = data.message;
            messageData.status = "danger";
            displayMessage(messageData)

          },
      });
}