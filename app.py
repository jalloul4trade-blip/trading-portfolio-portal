import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Givtrade - Client Portal",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 🎨 تنسيق الواجهة لتطابق بوابة Givtrade
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
# 🗄️ قاعدة بيانات الحسابات وتخزين الجلسة
# --------------------------------------------------
if 'accounts_list' not in st.session_state:
    st.session_state.accounts_list = [
        {"account_id": "7701924", "server": "Givtrade-Live 1", "type": "VIP Institutional", "deposit": 10000.0, "balance": 10450.0, "daily_pl": 450.0, "status": "SUSPENDED (معلق)"},
        {"account_id": "8840215", "server": "Givtrade-Live 2", "type": "Classic STP", "deposit": 5000.0, "balance": 4820.0, "daily_pl": -180.0, "status": "SUSPENDED (معلق)"},
    ]

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
# 🔝 الشريط العلوي للمنصة
# --------------------------------------------------
col_h1, col_h2, col_h3 = st.columns([2, 1, 1.2])
with col_h1:
    st.markdown(f"**Home** / Trader's Menu / **{menu_choice}**")
with col_h3:
    st.markdown("""
    <div style='text-align:right; font-size:13px;'>
        <b>Hasan Jalloul</b> <span style='background:#00e676; color:#000; padding:1px 6px; border-radius:4px; font-weight:bold;'>22752</span>
        &nbsp;|&nbsp; 🇬🇧 &nbsp;|&nbsp; 🚪 <a href='#' style='color:#64748b; text-decoration:none;'>Log out</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='margin:10px 0 25px 0; border:none; border-bottom:1px solid #e2e8f0;'>", unsafe_allow_html=True)

# --------------------------------------------------
# 📂 1. شاشة الحسابات (Accounts) مع الحسابات التلقائية
# --------------------------------------------------
if menu_choice == "Accounts":
    df_acc = pd.DataFrame(st.session_state.accounts_list)
    
    # العمليات الحسابية الآلية
    df_acc['equity'] = df_acc['balance'] + df_acc['daily_pl']
    df_acc['total_growth'] = df_acc['equity'] - df_acc['deposit']
    
    tot_deposit = df_acc['deposit'].sum()
    tot_equity = df_acc['equity'].sum()
    tot_daily_pl = df_acc['daily_pl'].sum()
    tot_net_growth = df_acc['total_growth'].sum()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("إجمالي الإيداعات التقديرية", f"${tot_deposit:,.2f}")
    m2.metric("السيولة الكلية (Live Equity)", f"${tot_equity:,.2f}")
    m3.metric("صافي أرباح/خسائر اليوم", f"${tot_daily_pl:+,.2f}", f"{(tot_daily_pl/tot_deposit)*100:+.2f}%")
    m4.metric("إجمالي النمو التراكمي", f"${tot_net_growth:+,.2f}", f"{(tot_net_growth/tot_deposit)*100:+.2f}%")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 قائمة الحسابات والتعقب اليومي")
    
    display_table = pd.DataFrame({
        "Account ID": df_acc['account_id'],
        "Server": df_acc['server'],
        "Account Type": df_acc['type'],
        "Deposit ($)": df_acc['deposit'].map('${:,.2f}'.format),
        "Balance ($)": df_acc['balance'].map('${:,.2f}'.format),
        "Daily P/L": df_acc['daily_pl'].map('{:+,.2f}$'.format),
        "Calculated Equity": df_acc['equity'].map('${:,.2f}'.format),
        "Total Net P/L": df_acc['total_growth'].map('{:+,.2f}$'.format),
        "Status": ["🔴 SUSPENDED / TRACKING ONLY" for _ in range(len(df_acc))]
    })
    
    st.dataframe(display_table, width='stretch', hide_index=True)

    st.markdown("---")

    col_entry1, col_entry2 = st.columns(2)

    with col_entry1:
        st.markdown("#### ➕ إضافة حساب جديد للمتابعة")
        with st.form("add_new_acc"):
            acc_num = st.text_input("رقم الحساب (Account Number)")
            acc_srv = st.selectbox("السيرفر", ["Givtrade-Live 1", "Givtrade-Live 2", "Givtrade-Pro STP"])
            acc_type = st.selectbox("نوع الحساب", ["VIP Institutional", "Classic STP", "Swap-Free Gold"])
            acc_dep = st.number_input("مبلغ الإيداع الأساسي ($)", min_value=100.0, value=5000.0, step=500.0)
            acc_bal = st.number_input("رصيد الحساب (Balance ($))", min_value=0.0, value=5000.0, step=500.0)
            acc_dpl = st.number_input("أرباح/خسائر اليوم ($)", value=0.0, step=50.0)
            
            btn_add = st.form_submit_button("إضافة الحساب", width='stretch', type="primary")
            if btn_add and acc_num:
                st.session_state.accounts_list.append({
                    "account_id": acc_num, "server": acc_srv, "type": acc_type,
                    "deposit": acc_dep, "balance": acc_bal, "daily_pl": acc_dpl,
                    "status": "SUSPENDED (معلق)"
                })
                st.success("تمت إضافة الحساب بنجاح!")
                st.rerun()

    with col_entry2:
        st.markdown("#### ⚙️ تحديث أرقام وأرباح حساب موجود")
        ids = [a['account_id'] for a in st.session_state.accounts_list]
        selected_id = st.selectbox("اختر رقم الحساب لتحديث أرقامه", ids)
        
        target_acc = next(a for a in st.session_state.accounts_list if a['account_id'] == selected_id)
        
        with st.form("update_acc"):
            u_dep = st.number_input("تحديث الإيداع ($)", value=float(target_acc['deposit']), step=500.0)
            u_bal = st.number_input("تحديث الرصيد (Balance ($))", value=float(target_acc['balance']), step=500.0)
            u_dpl = st.number_input("تحديث ربح/خسارة اليوم ($)", value=float(target_acc['daily_pl']), step=50.0)
            
            btn_update = st.form_submit_button("حفظ وتحديث الحسابات التلقائية", width='stretch')
            if btn_update:
                target_acc['deposit'] = u_dep
                target_acc['balance'] = u_bal
                target_acc['daily_pl'] = u_dpl
                st.success("تم التحديث وإعادة احتساب الأرباح والسيولة تلقائياً!")
                st.rerun()

# --------------------------------------------------
# 📂 2. شاشة الملف الشخصي (My Profile)
# --------------------------------------------------
elif menu_choice == "My Profile":
    col_prof_l, col_prof_r = st.columns([1.3, 1], gap="large")
    
    with col_prof_l:
        st.markdown("""
        <div class="portal-card">
            <h3 style="margin-top:0; font-size:18px; margin-bottom:20px;">Profile Information</h3>
            <table style="width:100%; border-collapse:collapse;">
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">First Name:</td><td style="font-weight:600;">Hasan</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Last Name:</td><td style="font-weight:600;">Jalloul</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Client ID:</td><td style="font-weight:600;">22752</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Date of birth:</td><td style="font-weight:600;">25-05-1987</td><td></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Password:</td><td style="font-weight:600;">••••••••</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Email:</td><td style="font-weight:600;">jalloul4tradefx@gmail.com</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Mobile Number:</td><td style="font-weight:600;">+971586747174</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding:12px 0; color:#64748b;">Communication Language:</td><td style="font-weight:600;">English</td><td style="text-align:right;"><span class="btn-green">Change</span></td></tr>
                <tr><td style="padding:12px 0; color:#64748b;">Country of Residence:</td><td style="font-weight:600;">United Arab Emirates</td><td></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

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
