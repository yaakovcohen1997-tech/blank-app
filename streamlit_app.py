import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
import streamlit as st
import datetime

st.set_page_config(page_title="מעקב חיסכון חכם", page_icon="💰", layout="centered")

st.title("💰 מעקב וחישוב חיסכון לטווח ארוך")
st.write("ברוך הבא לאפליקציית החיסכון האישית שלך!")

# תפריט ניווט פשוט למטה/למעלה
menu = ["היעדים שלי", "הוספת יעד חדש"]
choice = st.sidebar.selectbox("ניווט", menu)

# נתונים זמניים בתוך האפליקציה (בגרסה הבאה נחבר לגוגל שיטס)
if 'goals' not in st.session_state:
    st.session_state.goals = [
        {"name": "טלפון חדש", "target_amount": 4000, "date": datetime.date(2026, 12, 10), "monthly_pay": 650, "months_paid": 0, "ticker": "VOO"}
    ]

if choice == "היעדים שלי":
    st.subheader("📋 יעדי החיסכון הנוכחיים שלך")
    
    for i, goal in enumerate(st.session_state.goals):
        with st.container():
            st.write(f"### 📱 {goal['name']}")
            
            # חישוב חודשים שנותרו
            today = datetime.date.today()
            months_left = (goal['date'].year - today.year) * 12 + goal['date'].month - today.month
            if months_left <= 0: months_left = 1
            
            total_saved = goal['monthly_pay'] * goal['months_paid']
            progress = min(1.0, float(total_saved) / float(goal['target_amount']))
            
            st.progress(progress)
            st.write(f"🎯 **סכום היעד:** {goal['target_amount']} ₪ | 📅 **תאריך יעד:** {goal['date'].strftime('%d.%m.%Y')}")
            st.write(f"💵 **הפקדה חודשית קבועה:** {goal['monthly_pay']} ₪ (במדד {goal['ticker']})")
            st.write(f"📊 **סך הכל הופקד עד כה:** {total_saved} ₪ ({int(progress*100)}%)")
            
            # כפתור לעדכון חודש הפקדה
            if st.button(f"➕ סימון הפקדה חודשית עבור {goal['name']}", key=f"btn_{i}"):
                st.session_state.goals[i]['months_paid'] += 1
                st.rerun()
            st.divider()

elif choice == "הוספת יעד חדש":
    st.subheader("✨ יצירת יעד חיסכון חדש (חופשה, רכב וכו')")
    name = st.text_input("שם היעד (למשל: חופשה ביוון):")
    amount = st.number_input("סכום נדרש (₪):", min_value=100, value=5000)
    target_date = st.date_input("תאריך יעד:", value=datetime.date(2026, 12, 31))
    ticker = st.text_input("סימול מניה/מדד (למשל: VOO, AAPL):", value="VOO")
    monthly_pay = st.number_input("כמה תרצה להפקיד כל חודש בהוראת קבע (₪):", min_value=10, value=500)
    
    if st.button("💾 שמור יעד חדש"):
        st.session_state.goals.append({
            "name": name, "target_amount": amount, "date": target_date, "monthly_pay": monthly_pay, "months_paid": 0, "ticker": ticker
        })
        st.success("היעד נוסף בהצלחה! עבר ללשונית 'היעדים שלי'"))
