function sendOTP() {
    const email = document.getElementById('email');
    const otpverify = document.getElementsByClassName('otpverify')[0];

    let otp_val = Math.floor(Math.random() * 10000);

    let emailbody = `<h2>Your OTP is </h2>${otp_val}`;
    Email.send({
        SecureToken : "Your ID",
        To : email.value,
        From : "Your Email",
        Subject : "Email OTP using JavaScript",
        Body : emailbody,
    }).then(
        message => {
            if (message === "OK") {
                alert("OTP sent to your email " + email.value);

                otpverify.style.display = "flex";
                const otp_inp = document.getElementById('otp_inp');
                const otp_btn = document.getElementById('otp-btn');
                const otp_verified = document.getElementById('otp-verified');

                otp_btn.addEventListener('click', () => {
                    if (otp_inp.value == otp_val) {
                        alert("Email address verified...");
                        otp_verified.style.display = "block"; // Show the Next button
                        otp_verified.addEventListener('click', () => {
                            window.location.href = "/";
                        });
                    } else {
                        alert("Invalid OTP. You are not verified.");
                    }
                });
            } else {
                alert("Failed to send OTP. Please try again.");
            }
        }
    );
}
