


(function() {
    // https://dashboard.emailjs.com/admin/account
    emailjs.init('SmfdSxlZE-q5n5a1t');
})();

window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();

        emailjs.sendForm('service_rtx10be', 'template_j4mb7at', this)
            .then(function() {
                success();
            }, function(error) {
                console.log('FAILED...', error);
                
            });
    });
}

const Submit = () =>{
   document.getElementById('contact-form').Submit();
}

const success = () =>{
    console.log('sent');
    document.getElementById('submit-form').innerHTML='<input type="submit" value="Sent✔️" id="send">';
}

const failed = () => {
    document.getElementById('submit-form').innerHTML='<input type="submit" value="Failed❌" id="send">';
}