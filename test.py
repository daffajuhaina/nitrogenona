import streamlit as st

st.markdown(
    """
    <style>
    .st-emotion-cache-1sg9iaw{
        background-color: #B99E97;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .main {
        background-color: #F1F0EC; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
option = st.sidebar.selectbox('Menu',['Welcome','Introduction','About Concentration','Kadar b/v','Kadar b/b'])
if option == 'Welcome': 
    st.markdown("<h1 style='text-align: center; color: black;'>NitrogeNona</h1>", unsafe_allow_html=True)
    st.write('NitrogeNona merupakan Web Aplikasi yang dirancang untuk memudahkan pengguna mendapatkan pengetahuan mengenai kadar serta menghitung nilai kadar setelah titrasi, dengan hasil yang akurat dan efisien.')
    
    # Centering images using columns
    col1, cent_co, col3 = st.columns([1, 2, 1])
    with cent_co:
        st.image('Nitrogen_20240520_193526_0000.png', caption='')
        st.image('logo aka.png', caption='')

if option == 'Introduction':
    st.markdown("<h1 style='text-align: center; color: black ;'>Kelompok 11</h1>", unsafe_allow_html=True)
    st.write('Anggota Kelompok : ')
    st.image('Hallo LPK_20240512_140146_0000.png', caption='')

if option == 'About Concentration':
    st.markdown ('<h2 style="color:grey;">Penerapan Konsentrasi Larutan pada Analisis Titrimetri</h2>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:justify;">Agar lebih mudah memahami apa itu konsentrasi larutan, sebaiknya kita mengetahui tentang arti larutan itu sendiri. Larutan dalam ilmu kimia mempunyai arti yaitu campuran yang bersifat homogen dengan perbandingan komposisi sesuai dengan komponen penyusunnya. Salah satu contoh larutan dalam kimia adalah H2SO4 (asam sulfat). Jika larutan H2SO4 (asam sulfat) dialiri listrik, maka akan menghantarkan listrik.</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:justify;">Pada umumnya, suatu larutan terdiri satu jenis zat terlarut dan satu pelarut. Solvent (pelarut) dan Solut (zat yang terlarut) biasanya sudah sering didengar dan disebutkan. Solvent merupakan komponen yang dilihat secara fisik tidak berubah jika larutan terbentuk, sedangkan semua komponen yang ada pada Solut akan larut dalam pelarut.</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:justify;">Pada praktikum analisis titrimetri, kebanyakan perhitungan yang digunakan untuk menentukan besaran kadar analit menggunakan perhitungan %(b/v) dan %(b/b).</div>', unsafe_allow_html=True)

if option == 'Kadar b/v':
    st.markdown("<h1 style='text-align: center; color: choco;'>Kadar b/v</h1>", unsafe_allow_html=True)
    
    # Membuat tab di dalam menu Kadar b/v
    tab1, tab2 = st.tabs(["Pengertian", "Perhitungan"])

    with tab1:
        container = st.container(border=True)
        container.write("Satuan konsentrasi ini memiliki definisi terdapat sejumlah gram sampel di dalam 100 mL larutan. %(b/v) dapat didefinisikan juga sebagai %(g/mL). Jadi, untuk perhitungan %(b/v) harus menyisakan satuan gram dan mL dalam akhir perhitungan.")
        st.image('Screenshot (68).png', caption='')
        st.markdown('- Volume titran adalah larutan standar yang dijadikan titrant dalam proses titrasi')
        st.markdown('- Titrat dapat disesuaikan dengan unsur yang ingin ditetapkan besaran kadarnya')
        st.markdown('- Volume titrat adalah volume sampel dalam mL yang digunakan sebagai analit atau titrat dalam proses titrasi')
        st.markdown('- 10^-3 yang dimasukkan dalam perhitungan di atas digunakan untuk mengganti satuan mg menjadi satuan g')

    with tab2:
        st.markdown("<h2 style='text-align: center; color: black;'>Perhitungan Kadar b/v</h2>", unsafe_allow_html=True)
        volume_titran = st.number_input('Masukkan nilai volume titran (mL)')
        normalitas_titran = st.number_input('Masukkan nilai normalitas titran (N)')
        bobot_ekuivalen_sampel = st.number_input('Masukkan nilai bobot ekuivalen sampel (mg/mgrek)', 0)
        volume_titrat = st.number_input('Masukkan nilai volume titrat (mL)')
        hitung = st.button('Hitung kadar b/v')

        if hitung:
            kadar = volume_titran * normalitas_titran * bobot_ekuivalen_sampel / volume_titrat * 0.001 * 100
            st.success(f'Perhitungan kadar sampel adalah = {kadar}')

if option =='Kadar b/b':
    st.markdown("<h1 style='text-align: center; color: black;'>Kadar b/b</h1>", unsafe_allow_html=True)

    # Membuat tab di dalam menu Kadar b/v
    tab1, tab2 = st.tabs(["Pengertian", "Perhitungan"])

    with tab1:
        container = st.container(border=True)
        container.write('satuan konsentrasi ini memiliki definisi terdapat terdapat sejumlah gram sampel didalam 100g pelarut. %(b/b) dapat didefinisikan juga sebagai %(g/g). Jadi, untuk perhitungan %(b/b) harus menyisakan satuan gram dan gram yang tidak perlu dicoret (dihilangkan) dalam akhir perhitungan.')
        st.image('Screenshot (69).png', caption='')
        st.markdown('- Volume titran adalah larutan standar yang dijadikan titrant dalam proses titrasi')
        st.markdown('- Titrat dapat disesuaikan dengan unsur yang ingin ditetapkan besaran kadarnya')
        st.markdown('- gram (g) sampel berarti adalah massa sampel yang digunakan sebagai analit atau titrat dalam proses titrasi')

    with tab2:
        st.markdown("<h2 style='text-align: center; color: black;'>perhitungan kadar b/b</h2>", unsafe_allow_html=True)
        volume_titrant= st.number_input('masukan nilai volume titrant (mL)',)
        normalitas_titrant= st.number_input('masukan nilai normalitas titrant (N)',)
        bobot_ekuivalen_titrat= st.number_input('masukan nilai bobot ekuivalen titrat (mg/mgrek)',0)
        bobot_sampel= st.number_input('masukan nilai bobot sampel (g)',)
        hitung = st.button('hitung kadar b/b') 

        if hitung :
            kadar = volume_titrant*normalitas_titrant*bobot_ekuivalen_titrat/bobot_sampel*0.001*100
            st.success(f'perhitungan kadar sampel adalah = {kadar}')