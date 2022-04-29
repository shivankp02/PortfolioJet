$(document).ready(function(){

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;
    
    setProgressBar(current);
    
    $(".next").click(function(){
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });
    
    $(".previous").click(function(){
    
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();
    
    //Remove class active
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    
    //show the previous fieldset
    previous_fs.show();
    
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });
    
    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }
    
    $(".submit").click(function(){
    return false;
    })

    const setError = (input, message)=>{
        const parent=input.parentElement;
        const child = parent.querySelector('small');
        //add error message inside small 
        child.style.display = "block";
        child.innerHTML = message;
        //add error class
        parent.className = 'contact-form error';
    }
    const setSuccess = (input) => {
        const parent = input.parentElement;
        const child = parent.querySelector("small");
        child.style.display = "none";
    }

    $("#contact-name").keyup(function () {
        let name = document.getElementById('contact-name');
        if (name.value === "") {
            setError(name, "This field is required");
        }else {
            setSuccess(name);
        }
    });
    $("#contact-email").keyup(function(){
        let email = document.getElementById('contact-email');
        if (email.value === "") {
            setError(email, "This field is required");
        }
        else if (!email.value.match(/^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/)) {
            setError(email, "This Email is not valid");
        }
        else{
            setSuccess(email);
        }
    });
    
    $("#contact-phone").keyup(function () {
        let phone = document.getElementById('contact-phone');
        if (phone.value === "") {
            setError(phone, "This field is required");
        }
        else if (phone.value.length!=10) {
            setError(phone, "This Number is not valid");
        }
        else {
            setSuccess(phone);
        }
    });

    $("#contact-message").keyup(function () {
        let message = document.getElementById('contact-message');
        if (message.value === "") {
            setError(message, "This field is required");
        }else {
            setSuccess(message);
        }
    });

});

// Ajax calling
$('#enhance').on('click', function () {
    let obj = $("#obj").val();
    $.post(
        "/enhance",
        { obj: obj},
        function (response) {
            data = JSON.parse(response)
            console.log(data)
            // $("#cobj").html(response);
            var dataset = ``;
            for (let key in data) {
                console.log(key)
                dataset += `<ul><li><b>${key}</b></li>`;
                for (let i = 0; i < data[key].length;i++) {
                    dataset += `<li>${data[key][i]}</li>`
                }
                dataset += `</ul>`
            }
            $("#cobj").html(dataset);
        }
    );
})

$('#enhance').on('click', function () {
    let obj = $("#expr").val();
    $.post(
        "/enhance",
        { obj: obj},
        function (response) {
            data = JSON.parse(response)
            console.log(data)
            // $("#cobj").html(response);
            var dataset = ``;
            for (let key in data) {
                console.log(key)
                dataset += `<ul><li><b>${key}</b></li>`;
                for (let i = 0; i < data[key].length;i++) {
                    dataset += `<li>${data[key][i]}</li>`
                }
                dataset += `</ul>`
            }
            $("#cobj").html(dataset);
        }
    );
})