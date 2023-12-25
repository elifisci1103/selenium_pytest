YAYGIN PYTEST DECORATÖRLERİ

pytest.fixture: Bu dekoratör, bir test fonksiyonuna önce belirlenmiş durumları veya nesneleri sağlayan bir "fixture" (donatı) olarak işlev gören fonksiyonları belirtmek için kullanılır. Fixture'lar, testlerinizi düzenlemenize ve test sırasında kullanılan veri veya kaynakları önceden yapılandırmanıza olanak tanır.

pytest.mark: Bu dekoratör, test fonksiyonlarına etiketler eklemek için kullanılır. Etiketler, testleri gruplandırmak, filtrelemek veya özel çalışma koşulları eklemek için kullanışlıdır.

pytest.mark.parametrize: Bu dekoratör, bir test fonksiyonunu farklı parametre setleriyle birden çok kez çalıştırmak için kullanılır. Parametre setleri, testin çeşitli durumlarını kontrol etmek için kullanılabilir.
pytest.mark.skip ve pytest.mark.skipif: Bu dekoratörler, belirli testleri atlamak için kullanılır. pytest.mark.skip her zaman atlar, pytest.mark.skipif ise belirli bir koşulu karşıladığında atlar.
