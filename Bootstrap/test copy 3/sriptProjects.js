

Git1 = () =>{
    window.open("https://github.com/PulkitBxtra/LightWeb");
}
Dep1 = () =>{
    window.open("https://pulkitbxtra.github.io/LightWeb/");
}


(function() {
    // https://dashboard.emailjs.com/admin/account
    emailjs.init('SmfdSxlZE-q5n5a1t');
})();

window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('service_rtx10be', 'template_3pkd4sf', this)
            .then(function() {
                console.log('SUCCESS!');
            }, function(error) {
                console.log('FAILED...', error);
            });
    });
}