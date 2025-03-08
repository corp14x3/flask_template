# flask_template
 
bilinmesi gerekenler

{% include "______.html" %} direk olarak belirtilen html i ice aktarir
{% extends "______.html" %} bir html i ice aktarir ve icerisinde {% block ______ %} {% endblock %} olarak belirtilen yerleri istedigimiz gibi degistirmeye olanak tanir
{% block ______ %}{% endblock %} arasina yazili olan icerigi direk degistirmemize olanak sagliyor

pythondaki for if elif else hepsi html icerisinde ayni sekilde kullanilabiliyor 
pythondan gelen icerigi sayfada html de gostermek icin {{____}} yada {{____|safe}} bunlari kullanmak yeterli

birde sayfada birseyi yenileyebilmek icin 
<script>
    setInterval(function() {
        document.getElementById("mesaj").innerText
    }, 10);
</script>

bunu kullanmak yeterli