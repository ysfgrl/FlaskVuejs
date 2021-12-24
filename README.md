# Flask Vuejs  

Bu Proje Flask ve VueJs için örnek bir çalışmadır

## Hakkında

**Kullanılan teknolojiler**
    

 * **Backend**
    * Docker
    * Python
    * Flask
    * Jwt
    * MongoDb
   
 * **Frontend**
    * Docker
    * Vuejs
    * Nodejs
    * Npm
    * Bootstrap
    * Datatable (https://github.com/AndreSouzaAbreu/vue-data-table)
    * menu (https://github.com/akahon/vue-sidebar-menu-akahon)
   
 * **Geliştirme Ortamları**
   * WebStorm
   * PyCharm
   * DataGrip
   
 * **Test Araçları**
   * Postman
   * Chorome

 * **İşletim Sistemi**
   * Ubuntu
   

## Kurulum 
   * docker copmose up
   
## Api Test

 * Token al (POST http://localhost:9005/Auth/getToken)
   ```html
   Request Json:
   {
       "username":"***",
       "password":"**"
   }
   ```
   
 * Personel ekle (POST http://localhost:9005/Person/Add)
    ```html
    Request Json:
    {
        "name": "name",
        "password": "password",
        "surname": "surname",
        "tckn": "tckn",
        "username": "username"
    }
    ```
  
 * Personel Listesi (POST http://localhost:9005/Person/List)
   ```html
   Request Json:
   {
       "page":1,
       "limit":50"
   }
   ```
## Vuejs Test
   * Tarayıcıdan http://localhost:3000/Login
   * kullanıcı Ekleyin



   
    

## Authors
1. Yusuf Uğurlu

