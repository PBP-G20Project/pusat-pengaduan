function addDataProfile(e){
    e.preventDefault();
    const email = $("#email").val()
    const nama = $("#nama").val()
    const nik = $("#nik").val()
    const user_id = JSON.parse(document.getElementById('user_id').textContent);
    console.log(user_id)
    const data = {
                email,
                nama,
                nik,
                csrfmiddlewaretoken: token
    }
    $('#alert').empty();
      $.ajax({
      type: "POST",
      url: loadUrl,
      data: data,
      dataType: "json",
      success: function () {
      $('#alert').append(
        `
        <div class="mt-1 text-green-500 text-l w-full text-info">
          <div>
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          <span class="label-text">Akun telah berhasil diubah</span>
          </div>
        </div>
        `
      )},
      error: function () {
        $('#alert').append(
        `
        <div class="mt-1 text-red-500 text-l w-full text-info">
          <div>
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
          <span class="label-text">Semua isian harus dilengkapi!</span>
          </div>
        </div>
        `
      )}
    });
}
$(document).ready(function(){
  $("#submitBtnProfile").click(addDataProfile)
});