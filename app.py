import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Givtrade - Client Portal",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 🎨 تنسيق الواجهة الرسمي
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1e293b;
    }
    section[data-testid="stSidebar"] * {
        color: #94a3b8;
    }
    .portal-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .btn-green {
        background-color: #00c853;
        color: white;
        border-radius: 6px;
        padding: 6px 14px;
        font-weight: 600;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 🗄️ تهيئة البيانات القابلة للتعديل في الجلسة
# --------------------------------------------------
if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {
        "first_name": "Hasan",
        "last_name": "Jalloul",
        "client_id": "22752",
        "dob": "25-05-1987",
        "email": "jalloul4tradefx@gmail.com",
        "phone": "+971586747174",
        "lang": "English",
        "country": "United Arab Emirates",
        "verified": False
    }

if 'accounts_df' not in st.session_state:
    st.session_state.accounts_df = pd.DataFrame([
        {"Account ID": "7701924", "Server": "Givtrade-Live 1", "Type": "VIP Institutional", "Deposit": 10000.0, "Balance": 10450.0, "Daily P/L": 450.0, "Status": "🔴 SUSPENDED"},
        {"Account ID": "8840215", "Server": "Givtrade-Live 2", "Type": "Classic STP", "Deposit": 5000.0, "Balance": 4820.0, "Daily P/L": -180.0, "Status": "🔴 SUSPENDED"},
    ])

# --------------------------------------------------
# 🧭 القائمة الجانبية (Sidebar)
# --------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:#00e676; margin-bottom:20px;'><span style='background:#00e676; color:#000; padding:2px 8px; border-radius:6px; font-weight:900;'>G</span> Givtrade</h2>", unsafe_allow_html=True)
    
    st.caption("TRADER'S MENU")
    menu_choice = st.radio(
        label="Trader Menu Options",
        options=["Accounts", "My Profile", "Funds", "Upload Documents", "Messages", "Help Desk", "Economic Calendar"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("IB MENU")
    st.markdown("💼 Request IB")

# --------------------------------------------------
# 🔝 الشريط العلوي للمنصة (ديناميكي ومربوط بالبيانات)
# --------------------------------------------------
prof = st.session_state.profile_data
col_h1, col_h2, col_h3 = st.columns([2, 1, 1.3])
with col_h1:
    st.markdown(f"**Home** / Trader's Menu / **{menu_choice}**")
with col_h3:
    st.markdown(f"""
    <div style='text-align:right; font-size:13px;'>
        <b>{prof['first_name']} {prof['last_name']}</b> <span style='background:#00e676; color:#000; padding:1px 6px; border-radius:4px; font-weight:bold;'>{prof['client_id']}</span>
        &nbsp;|&nbsp; 🇬🇧 &nbsp;|&nbsp; 🚪 <a href='#' style='color:#64748b; text-decoration:none;'>Log out</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='margin:10px 0 25px 0; border:none; border-bottom:1px solid #e2e8f0;'>", unsafe_allow_html=True)

# --------------------------------------------------
# 📂 1. شاشة الحسابات (Accounts) - تعديل مباشر مثل Excel
# --------------------------------------------------
if menu_choice == "Accounts":
    
    # حساب المعادلات التلقائية من الجدول الحالي
    df = st.session_state.accounts_df.copy()
    
    # تحويل القيم لأرقام لضمان العمليات الحسابية
    df['Deposit'] = pd.to_numeric(df['Deposit'], errors='coerce').fillna(0)
    df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce').fillna(0)
    df['Daily P/L'] = pd.to_numeric(df['Daily P/L'], errors='coerce').fillna(0)
    
    df['Calculated Equity'] = df['Balance'] + df['Daily P/L']
    df['Total Net P/L'] = df['Calculated Equity'] - df['Deposit']
    
    tot_deposit = df['Deposit'].sum()
    tot_equity = df['Calculated Equity'].sum()
    tot_daily_pl = df['Daily P/L'].sum()
    tot_net_growth = df['Total Net P/L'].sum()

    # كروت الإحصائيات في الأعلى
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("إجمالي الإيداعات التقديرية", f"${tot_deposit:,.2f}")
    m2.metric("السيولة الكلية (Live Equity)", f"${tot_equity:,.2f}")
    m3.metric("صافي أرباح/خسائر اليوم", f"${tot_daily_pl:+,.2f}", f"{(tot_daily_pl/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")
    m4.metric("إجمالي النمو التراكمي", f"${tot_net_growth:+,.2f}", f"{(tot_net_growth/tot_deposit)*100:+.2f}%" if tot_deposit > 0 else "0.00%")

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.subheader("📋 قائمة الحسابات (اضغط مرتين على أي رقم للتعديل الفوري)")
    with col_t2:
        st.info("💡 يمكنك إضافة صفوف جديدة مباشرة من أسفل الجدول")

    # جدول تفاعلي بالكامل يسمح بالتعديل المباشر وإضافة وحذف الحسابات
    edited_df = st.data_editor(
        st.session_state.accounts_df,
        num_rows="dynamic", # يسمح بإضافة وحذف صفوف
        width='stretch',
        use_container_width=True,
        column_config={
            "Deposit": st.column_config.NumberColumn("Deposit ($)", format="$%.2f"),
            "Balance": st.column_config.NumberColumn("Balance ($)", format="$%.2f"),
            "Daily P/L": st.column_config.NumberColumn("Daily P/L ($)", format="$%.2f"),
            "Status": st.column_config.SelectboxColumn("Status", options=["🔴 SUSPENDED", "🟢 ACTIVE", "🟡 PENDING"]),
            "Server": st.column_config.SelectboxColumn("Server", options=["Givtrade-Live 1", "Givtrade-Live 2", "Givtrade-Pro STP"]),
            "Type": st.column_config.SelectboxColumn("Account Type", options=["VIP Institutional", "Classic STP", "Swap-Free Gold"])
        }
    )

    # حفظ التعديلات فوراً عند تغيير أي خلية
    if not edited_df.equals(st.session_state.accounts_df):
        st.session_state.accounts_df = edited_df
        st.rerun()

    st.markdown("---")
    
    # جدول عرض النتائج المحسوبة آلياً
    st.subheader("📊 ملخص الحسابات والسيولة المحسوبة آلياً")
    summary_view = pd.DataFrame({
        "Account ID": df['Account ID'],
        "Server": df['Server'],
        "Calculated Equity (السيولة الحية)": df['Calculated Equity'].map('${:,.2f}'.format),
        "Total Profit / Loss (الربح الإجمالي)": df['Total Net P/L'].map('{:+,.2f}$'.format),
        "ROI %": ((df['Total Net P/L'] / df['Deposit']) * 100).map('{:+.2f}%'.format),
        "Status": df['Status']
    })
    st.dataframe(summary_view, width='stretch', hide_index=True)

# --------------------------------------------------
# 📂 2. شاشة الملف الشخصي (My Profile) مع إمكانية التعديل
# --------------------------------------------------
elif menu_choice == "My Profile":
    
    col_prof_l, col_prof_r = st.columns([1.3, 1], gap="large")
    
    with col_prof_l:
        st.markdown(f"""
        <div class="portal-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">Profile Information</h3>
            <table style="width:100%; border-collapse:collapse;">
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">First Name:</td><td style="font-weight:600;">{prof['first_name']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Last Name:</td><td style="font-weight:600;">{prof['last_name']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Client ID:</td><td style="font-weight:600;">{prof['client_id']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Date of birth:</td><td style="font-weight:600;">{prof['dob']}</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Password:</td><td style="font-weight:600;">••••••••</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Email:</td><td style="font-weight:600;">{prof['email']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Mobile Number:</td><td style="font-weight:600;">{prof['phone']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Communication Language:</td><td style="font-weight:600;">{prof['lang']}</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr><td style="padding:12px 0; color:#64748b;">Country of Residence:</td><td style="font-weight:600;">{prof['country']}</td><td></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # زر منسدل لتعديل بيانات البروفايل في أي وقت
        with st.expander("✏️ تعديل بيانات الملف الشخصي (Profile Settings)"):
            with st.form("edit_profile_form"):
                f_name = st.text_input("First Name", value=prof['first_name'])
                l_name = st.text_input("Last Name", value=prof['last_name'])
                c_id = st.text_input("Client ID", value=prof['client_id'])
                d_ob = st.text_input("Date of Birth", value=prof['dob'])
                em = st.text_input("Email", value=prof['email'])
                ph = st.text_input("Mobile Number", value=prof['phone'])
                ct = st.text_input("Country", value=prof['country'])
                save_prof = st.form_submit_button("حفظ بيانات البروفايل الجديدة", type="primary")
                if save_prof:
                    st.session_state.profile_data.update({
                        "first_name": f_name, "last_name": l_name, "client_id": c_id,
                        "dob": d_ob, "email": em, "phone": ph, "country": ct
                    })
                    st.success("تم تحديث البروفايل بنجاح!")
                    st.rerun()

    with col_prof_r:
        st.markdown("""
        <div class="portal-card">
            <div style="background:#fff1f2; color:#e11d48; padding:8px 12px; border-radius:6px; font-size:13px; font-weight:600; margin-bottom:20px;">
                🔴 Your profile is not verified
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="color:#64748b; font-size:14px;">Verification Documents</span>
                <span style="background:#00bcd4; color:white; padding:2px 8px; border-radius:4px; font-size:12px; font-weight:bold;">Pending</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.info(f"قسم {menu_choice} قيد التطوير.")
