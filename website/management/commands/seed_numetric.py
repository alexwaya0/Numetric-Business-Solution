from django.core.management.base import BaseCommand

from website.models import (
    Category,
    Certification,
    CoreValue,
    ProfessionalAffiliation,
    Service,
    SiteSettings,
    Testimonial,
    Post,
)


class Command(BaseCommand):

    help = (
        "Populate the Numetric Business Solution website "
        "with initial company, service, blog and brand content."
    )

    # ======================================================
    # SERVICES
    # ======================================================

    SERVICES = [
        {
            "number": 1,
            "name": "Bookkeeping & Financial Reporting",
            "slug": "bookkeeping-financial-reporting",
            "tagline": (
                "Clean books. Clear numbers. "
                "Real confidence in your business."
            ),
            "overview": (
                "Every good business decision starts with accurate "
                "numbers. At Numetric, we handle the day-to-day "
                "recording of your transactions and turn them into "
                "financial statements you can actually trust — so "
                "you always know where your business stands, not "
                "just at year-end, but every month."
            ),
            "services": "\n".join(
                [
                    "Bookkeeping",
                    "Financial Statement Preparation",
                    "Management Reporting",
                    "Accounts Payable & Receivable Management",
                    "Bank Reconciliations",
                    "Fixed Asset Register Management",
                    "Accounting System Setup & Support",
                    "Accounting Policy Development",
                ]
            ),
            "who_its_for": (
                "Startups, SMEs, schools, hospitals, NGOs, "
                "associations, and organizations that need dependable, "
                "up-to-date books — whether you have no in-house "
                "finance function yet, or you want an experienced hand "
                "to keep your existing records accurate and audit-ready."
            ),
        },
        {
            "number": 2,
            "name": "Tax Planning & Compliance",
            "slug": "tax-planning-compliance",
            "tagline": (
                "Stay compliant. Stay ahead. "
                "Never let tax catch you off guard."
            ),
            "overview": (
                "Kenya's tax environment moves fast, and the cost "
                "of getting it wrong — penalties, blocked TCCs, KRA "
                "disputes — is high. We manage your tax obligations "
                "proactively, not reactively, so compliance is handled "
                "correctly and on time, and you're positioned to plan "
                "ahead rather than scramble at deadlines."
            ),
            "services": "\n".join(
                [
                    "Tax Planning & Advisory",
                    "Corporate Tax Compliance",
                    "Individual Tax Services",
                    "VAT Compliance",
                    "Withholding Tax",
                    "Capital Gains Tax",
                    "Tax Health Checks",
                    "KRA Audit Support",
                    "Tax Dispute Resolution",
                ]
            ),
            "who_its_for": (
                "Business owners who want tax handled by someone "
                "who understands KRA processes from the inside — "
                "and who'd rather prevent a problem than fix one "
                "after it lands."
            ),
        },
        {
            "number": 3,
            "name": "Payroll Management",
            "slug": "payroll-management",
            "tagline": (
                "Pay your people right, every time."
            ),
            "overview": (
                "Payroll is one of the few areas where a mistake is "
                "immediately visible to your team. We run accurate, "
                "compliant payroll every cycle — statutory deductions "
                "handled correctly, records maintained properly, and "
                "your employees paid on time, without you having to "
                "chase the details."
            ),
            "services": "\n".join(
                [
                    "Payroll Processing",
                    "PAYE & Payroll Tax",
                    "Statutory Payroll Compliance",
                    "Payroll Reports",
                    "Employee Records Management",
                ]
            ),
            "who_its_for": (
                "Businesses of any size that want payroll off their "
                "plate entirely — accurate, confidential, and compliant, "
                "without needing an in-house payroll administrator."
            ),
        },
        {
            "number": 4,
            "name": "Management Accounting & Insights",
            "slug": "management-accounting-insights",
            "tagline": (
                "Numbers that don't just report the past — "
                "they guide what's next."
            ),
            "overview": (
                "Bookkeeping tells you what happened. Management "
                "accounting tells you what to do about it. We go "
                "beyond compliance to give you budgets, forecasts, "
                "and performance insights that support real "
                "decision-making — so you're running your business "
                "on evidence, not instinct."
            ),
            "services": "\n".join(
                [
                    "Management Accounts",
                    "Budgeting",
                    "Financial Planning & Forecasting",
                    "Cash Flow Management",
                    "Profitability Analysis",
                    "Cost Analysis",
                    "Variance Analysis",
                    "Key Performance Indicators",
                    "Business Performance Reviews",
                    "Financial Analysis & Insights",
                ]
            ),
            "who_its_for": (
                "Business owners and boards who want to understand "
                "why the numbers are what they are — and use that "
                "understanding to plan pricing, spending, and growth "
                "with more confidence."
            ),
        },
        {
            "number": 5,
            "name": "Virtual CFO & Strategic Advisory",
            "slug": "virtual-cfo-strategic-advisory",
            "tagline": (
                "Practical advice, from people who know "
                "the numbers behind your business."
            ),
            "overview": (
                "Providing experienced financial leadership and "
                "strategic support to help businesses improve "
                "performance, manage complexity, and make better "
                "financial decisions."
            ),
            "services": "\n".join(
                [
                    "Virtual & Fractional CFO Services",
                    "Business Strategy",
                    "Financial Strategy",
                    "Business Growth & Expansion Advisory",
                    "Cash Flow Advisory",
                    "Cost Optimisation",
                    "Business Process Improvement",
                    "Risk Management",
                    "Internal Control Advisory",
                    "Company Secretarial Services",
                    "Feasibility Studies",
                    "Business Valuation",
                    "Financial Due Diligence",
                ]
            ),
            "who_its_for": (
                "Business owners who want more than a once-a-year "
                "accountant — someone who understands their numbers "
                "well enough to help think through what comes next."
            ),
        },
        {
            "number": 6,
            "name": "Financial Training & Team Upskilling",
            "slug": "financial-training-team-upskilling",
            "tagline": (
                "Build financial capability inside your team, "
                "not just outside it."
            ),
            "overview": (
                "The strongest businesses don't outsource all their "
                "financial understanding — they build it internally "
                "too. We run practical, hands-on training for business "
                "owners and teams, so your people are confident with "
                "the tools, compliance requirements, and controls "
                "that protect and grow the business."
            ),
            "services": "\n".join(
                [
                    "Financial Management Training",
                    "Accounting & Bookkeeping Training",
                    "Tax & Compliance Training",
                    "eTIMS Training",
                    "Financial Reporting Training",
                    "Budgeting & Cash Flow Training",
                    "Internal Controls Training",
                    "Team Financial Skills Development",
                ]
            ),
            "who_its_for": (
                "Business owners and teams who want to strengthen "
                "their own financial literacy and controls — not "
                "just outsource the work, but understand it."
            ),
        },
        {
            "number": 7,
            "name": "Audit & Assurance",
            "slug": "audit-assurance",
            "tagline": (
                "Independent assurance that builds confidence, "
                "strengthens governance, and supports reliable "
                "financial reporting."
            ),
            "overview": (
                "Independent assurance that builds confidence, "
                "strengthens governance, and supports reliable "
                "financial reporting."
            ),
            "services": "\n".join(
                [
                    "Statutory Financial Statement Audits",
                    "Independent Assurance Services",
                    "Internal Control Reviews",
                    "Audit Readiness Assessments",
                    "Financial Reporting Compliance Reviews",
                    "Risk & Governance Reviews",
                ]
            ),
            "who_its_for": (
                "Businesses, boards, and stakeholders who need "
                "independent, credible assurance over financial "
                "reporting and internal controls."
            ),
        },
    ]

    # ======================================================
    # BLOG CATEGORIES
    # ======================================================

    CATEGORIES = [
        {
            "name": "Accounting & Finance",
            "slug": "accounting-finance",
            "description": (
                "Practical accounting and financial management "
                "insights for growing businesses."
            ),
        },
        {
            "name": "Tax & Compliance",
            "slug": "tax-compliance",
            "description": (
                "Practical guidance on tax, compliance and "
                "financial obligations in Kenya."
            ),
        },
        {
            "name": "Business Growth",
            "slug": "business-growth",
            "description": (
                "Financial perspectives to help businesses "
                "grow sustainably."
            ),
        },
        {
            "name": "Leadership & Strategy",
            "slug": "leadership-strategy",
            "description": (
                "Strategic financial thinking for business "
                "owners and leaders."
            ),
        },
    ]

    # ======================================================
    # BLOG POSTS
    # ======================================================

    POSTS = [
        {
            "category": "Accounting & Finance",
            "title": (
                "Why Every Business Needs Accurate Monthly "
                "Financial Reports"
            ),
            "slug": (
                "why-every-business-needs-accurate-monthly-"
                "financial-reports"
            ),
            "excerpt": (
                "Monthly financial reporting gives business "
                "owners a clearer picture of performance, "
                "cash flow and emerging risks."
            ),
            "body": (
                "Financial statements should not be something "
                "a business only looks at when the year ends. "
                "Regular financial reporting gives owners and "
                "management a current view of what is happening "
                "inside the business.\n\n"
                "Monthly reports can highlight changes in revenue, "
                "expenses, profitability and cash flow before they "
                "become larger problems.\n\n"
                "For growing businesses, timely reporting also "
                "creates a stronger foundation for budgeting, "
                "planning and investment decisions.\n\n"
                "The goal is not simply to produce reports. It is "
                "to turn reliable numbers into information that "
                "helps business leaders make better decisions."
            ),
        },
        {
            "category": "Accounting & Finance",
            "title": (
                "5 Financial Numbers Every Business Owner "
                "Should Know"
            ),
            "slug": (
                "5-financial-numbers-every-business-owner-"
                "should-know"
            ),
            "excerpt": (
                "Revenue alone does not tell the full story. "
                "Here are five financial measures every business "
                "owner should understand."
            ),
            "body": (
                "Business owners do not need to become accountants "
                "to understand their numbers. But they do need to "
                "know which numbers matter.\n\n"
                "Revenue shows how much the business is generating, "
                "while gross profit helps reveal how efficiently "
                "the business delivers its products or services.\n\n"
                "Operating expenses, net profit and cash flow provide "
                "another layer of insight into sustainability and "
                "financial health.\n\n"
                "Understanding these numbers regularly can help "
                "owners identify trends and take action earlier."
            ),
        },
        {
            "category": "Business Growth",
            "title": (
                "How to Improve Cash Flow Without Slowing "
                "Your Growth"
            ),
            "slug": (
                "how-to-improve-cash-flow-without-slowing-"
                "your-growth"
            ),
            "excerpt": (
                "Healthy cash flow is essential for growth. "
                "Here are practical ways to improve it without "
                "putting the brakes on your business."
            ),
            "body": (
                "A profitable business can still experience cash "
                "flow pressure. The timing of customer payments, "
                "supplier obligations and operating expenses can "
                "create difficult periods even when sales are strong.\n\n"
                "Businesses can improve cash flow by tightening "
                "receivables management, reviewing payment terms, "
                "monitoring expenses and forecasting cash requirements.\n\n"
                "The key is to manage cash proactively rather than "
                "waiting until a shortage becomes urgent."
            ),
        },
        {
            "category": "Tax & Compliance",
            "title": (
                "Tax Compliance in Kenya: What Every Business "
                "Should Know"
            ),
            "slug": (
                "tax-compliance-in-kenya-what-every-business-"
                "should-know"
            ),
            "excerpt": (
                "Tax compliance is more than meeting deadlines. "
                "A proactive approach can reduce risk and improve "
                "financial planning."
            ),
            "body": (
                "Tax obligations can become increasingly complex "
                "as a business grows. Different taxes, filing "
                "requirements and changing regulations require "
                "consistent attention.\n\n"
                "Businesses should maintain accurate records, "
                "understand their applicable obligations and "
                "monitor filing and payment deadlines.\n\n"
                "Good tax management also involves planning ahead. "
                "The objective should be to remain compliant while "
                "making informed financial decisions."
            ),
        },
        {
            "category": "Accounting & Finance",
            "title": (
                "Common Bookkeeping Mistakes That Cost "
                "Businesses Money"
            ),
            "slug": (
                "common-bookkeeping-mistakes-that-cost-"
                "businesses-money"
            ),
            "excerpt": (
                "Small bookkeeping errors can create bigger "
                "financial problems. Learn which mistakes businesses "
                "should avoid."
            ),
            "body": (
                "Poor bookkeeping can affect much more than the "
                "appearance of financial records. It can influence "
                "tax calculations, cash management and decision-making.\n\n"
                "Common issues include missing transactions, poor "
                "reconciliation, mixing personal and business expenses "
                "and failing to maintain supporting documentation.\n\n"
                "A consistent bookkeeping process makes it easier "
                "to identify discrepancies and produce reliable "
                "financial information."
            ),
        },
        {
            "category": "Tax & Compliance",
            "title": (
                "Understanding VAT: A Practical Guide for "
                "Kenyan Businesses"
            ),
            "slug": (
                "understanding-vat-a-practical-guide-for-"
                "kenyan-businesses"
            ),
            "excerpt": (
                "VAT affects pricing, invoicing, records and "
                "cash flow. Understanding the fundamentals can "
                "help businesses manage it more effectively."
            ),
            "body": (
                "VAT is an important consideration for businesses "
                "that fall within the applicable requirements. "
                "It affects how transactions are recorded and how "
                "businesses manage their tax obligations.\n\n"
                "Accurate records and timely compliance are essential "
                "for maintaining reliable VAT information.\n\n"
                "Businesses should also consider the effect VAT has "
                "on pricing, cash flow and customer relationships."
            ),
        },
        {
            "category": "Leadership & Strategy",
            "title": (
                "When Should Your Business Consider a "
                "Virtual CFO?"
            ),
            "slug": (
                "when-should-your-business-consider-a-"
                "virtual-cfo"
            ),
            "excerpt": (
                "A Virtual CFO can give growing businesses access "
                "to senior financial thinking without the cost of "
                "a full-time executive."
            ),
            "body": (
                "As businesses grow, financial decisions become "
                "more complex. Owners may need stronger forecasting, "
                "cash flow management, financial controls and "
                "strategic analysis.\n\n"
                "A Virtual CFO provides experienced financial "
                "leadership on a flexible basis, helping businesses "
                "make better decisions without necessarily creating "
                "a full-time executive position.\n\n"
                "The right time to consider this support is when "
                "financial complexity begins to outgrow the existing "
                "finance function."
            ),
        },
        {
            "category": "Business Growth",
            "title": (
                "Budgeting for Business Growth: "
                "Where Should You Start?"
            ),
            "slug": (
                "budgeting-for-business-growth-where-"
                "should-you-start"
            ),
            "excerpt": (
                "A useful budget should help management make "
                "decisions, allocate resources and prepare for "
                "different scenarios."
            ),
            "body": (
                "A budget is more than a spreadsheet of expected "
                "income and expenses. It is a financial expression "
                "of the business plan.\n\n"
                "Start by understanding historical performance, "
                "then establish realistic revenue expectations "
                "and identify the costs required to support them.\n\n"
                "A good budget should also be reviewed regularly "
                "against actual results so management can understand "
                "where performance differs from expectations."
            ),
        },
        {
            "category": "Business Growth",
            "title": (
                "How Financial Forecasting Helps You Make "
                "Better Decisions"
            ),
            "slug": (
                "how-financial-forecasting-helps-you-make-"
                "better-decisions"
            ),
            "excerpt": (
                "Forecasting helps businesses look forward rather "
                "than simply reacting to what has already happened."
            ),
            "body": (
                "Historical financial information tells you what "
                "has happened. Forecasting helps you think about "
                "what could happen next.\n\n"
                "Businesses can use forecasts to model revenue, "
                "expenses, cash requirements and potential growth "
                "scenarios.\n\n"
                "The value of forecasting comes from using it as "
                "a decision-making tool rather than treating it "
                "as a static document."
            ),
        },
        {
            "category": "Tax & Compliance",
            "title": (
                "Payroll Compliance: What Employers Need "
                "to Get Right"
            ),
            "slug": (
                "payroll-compliance-what-employers-need-"
                "to-get-right"
            ),
            "excerpt": (
                "Accurate payroll protects employees and employers. "
                "Here are some of the key areas businesses need "
                "to manage carefully."
            ),
            "body": (
                "Payroll is both a financial and operational "
                "responsibility. Errors can affect employees "
                "directly and create compliance concerns for "
                "the employer.\n\n"
                "Businesses need reliable employee records, "
                "accurate calculations and consistent processes "
                "for applicable statutory obligations.\n\n"
                "A structured payroll process helps reduce errors "
                "and gives management confidence that employees "
                "are being paid accurately and on time."
            ),
        },
        {
            "category": "Tax & Compliance",
            "title": (
                "eTIMS and Your Business: What You Need to Know"
            ),
            "slug": (
                "etims-and-your-business-what-you-need-to-know"
            ),
            "excerpt": (
                "Digital tax invoicing has become an important "
                "part of business compliance. Here's why businesses "
                "need a reliable process."
            ),
            "body": (
                "Digital invoicing requirements have changed how "
                "many businesses manage sales documentation and "
                "tax records.\n\n"
                "Businesses should ensure their invoicing processes "
                "are properly integrated with their accounting "
                "records and internal controls.\n\n"
                "The objective is not simply compliance. A well-managed "
                "digital invoicing process can also improve record "
                "keeping and financial visibility."
            ),
        },
        {
            "category": "Accounting & Finance",
            "title": (
                "How to Know If Your Business Is Actually Profitable"
            ),
            "slug": (
                "how-to-know-if-your-business-is-actually-profitable"
            ),
            "excerpt": (
                "Strong sales do not automatically mean strong "
                "profits. Learn how to look beyond revenue."
            ),
            "body": (
                "Revenue is one of the most visible business "
                "numbers, but it is not the same as profitability.\n\n"
                "To understand profitability, businesses need to "
                "look at direct costs, operating expenses, financing "
                "costs and the timing of income and expenditure.\n\n"
                "Regular management reporting can help owners "
                "understand which products, services or customers "
                "are contributing most to the bottom line."
            ),
        },
        {
            "category": "Leadership & Strategy",
            "title": (
                "Internal Controls Every Growing Business "
                "Should Have"
            ),
            "slug": (
                "internal-controls-every-growing-business-"
                "should-have"
            ),
            "excerpt": (
                "As a business grows, informal processes may no "
                "longer be enough. Strong internal controls help "
                "protect assets and reduce risk."
            ),
            "body": (
                "Internal controls provide structure around how "
                "financial and operational activities are performed.\n\n"
                "Examples include approval processes, segregation "
                "of duties, reconciliations, access controls and "
                "regular management reviews.\n\n"
                "Controls should be practical and proportionate "
                "to the size and complexity of the business."
            ),
        },
        {
            "category": "Leadership & Strategy",
            "title": (
                "Financial Training: Why Your Team Needs to "
                "Understand the Numbers"
            ),
            "slug": (
                "financial-training-why-your-team-needs-to-"
                "understand-the-numbers"
            ),
            "excerpt": (
                "Financial capability should not sit with one "
                "person. Building financial understanding across "
                "your team can strengthen the business."
            ),
            "body": (
                "Employees make financial decisions every day, "
                "whether they are approving expenses, managing "
                "customers, purchasing supplies or preparing reports.\n\n"
                "Financial training helps teams understand the "
                "impact of these decisions and strengthens the "
                "connection between daily operations and business "
                "performance.\n\n"
                "The strongest training is practical, relevant "
                "and connected to the systems and processes "
                "employees actually use."
            ),
        },
        {
            "category": "Leadership & Strategy",
            "title": (
                "From Compliance to Strategy: The Changing "
                "Role of the Accountant"
            ),
            "slug": (
                "from-compliance-to-strategy-the-changing-"
                "role-of-the-accountant"
            ),
            "excerpt": (
                "Modern finance support should do more than "
                "prepare accounts. It should help leaders "
                "understand what the numbers mean."
            ),
            "body": (
                "Accounting has traditionally been associated "
                "with record keeping, reporting and compliance. "
                "Those responsibilities remain essential, but "
                "businesses increasingly need more from their "
                "finance partners.\n\n"
                "Financial information can help leaders understand "
                "performance, manage risk, plan investment and "
                "identify opportunities for growth.\n\n"
                "This is where accounting becomes a strategic "
                "business function — turning accurate information "
                "into useful insight."
            ),
        },
    ]

    # ======================================================
    # CORE VALUES
    # ======================================================

    CORE_VALUES = [
        {
            "number": 1,
            "name": "Integrity",
            "description": (
                "We do what's right."
            ),
        },
        {
            "number": 2,
            "name": "Excellence",
            "description": (
                "We never stop improving."
            ),
        },
        {
            "number": 3,
            "name": "Partnership",
            "description": (
                "We grow stronger together."
            ),
        },
        {
            "number": 4,
            "name": "Impact",
            "description": (
                "We create value that lasts."
            ),
        },
    ]

    # ======================================================
    # TESTIMONIALS
    # ======================================================

    TESTIMONIALS = [
        {
            "quote": (
                "Numetric has been a reliable partner in managing "
                "our accounting and financial reporting. Their "
                "work is accurate and timely. Good work!"
            ),
            "name": "Managing Director",
            "role": "Managing Director",
            "company": "SME Client",
            "display_order": 1,
        },
        {
            "quote": (
                "The team at Numetric is professional, responsive "
                "and easy to work with."
            ),
            "name": "Business Owner",
            "role": "Business Owner",
            "company": "Nairobi",
            "display_order": 2,
        },
        {
            "quote": (
                "They take the time to understand our business "
                "and provide useful insights that help us manage "
                "our finances effectively."
            ),
            "name": "Director",
            "role": "Director",
            "company": "Private Company",
            "display_order": 3,
        },
    ]

    # ======================================================
    # CREDENTIALS
    # ======================================================

    CERTIFICATIONS = [
        {
            "name": "CPA (K)",
            "description": (
                "Certified Public Accountant (Kenya)"
            ),
            "display_order": 1,
        },
        {
            "name": "QuickBooks Certified",
            "description": (
                "QuickBooks Certified"
            ),
            "display_order": 2,
        },
        {
            "name": "Odoo Certified",
            "description": (
                "Odoo Certified"
            ),
            "display_order": 3,
        },
    ]

    AFFILIATIONS = [
        {
            "name": (
                "Institute of Certified Public Accountants "
                "of Kenya (ICPAK)"
            ),
            "description": (
                "Professional affiliation with ICPAK."
            ),
            "display_order": 1,
        },
    ]

    # ======================================================
    # HANDLE
    # ======================================================

    def handle(self, *args, **options):

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Starting Numetric Business Solution seed..."
            )
        )
        self.stdout.write("")

        self.seed_site_settings()
        self.seed_services()
        self.seed_categories()
        self.seed_core_values()
        self.seed_testimonials()
        self.seed_certifications()
        self.seed_affiliations()
        self.seed_posts()

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Numetric content successfully seeded."
            )
        )
        self.stdout.write("")

    # ======================================================
    # SITE SETTINGS
    # ======================================================

    def seed_site_settings(self):

        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                "company_name": (
                    "Numetric Business Solution"
                ),

                "tagline": (
                    "Financial clarity for better "
                    "business decisions."
                ),

                "email": (
                    "info@numetricbusiness.co.ke"
                ),

                "managing_partner_email": (
                    "managing.partner@numetricbusiness.co.ke"
                ),

                "accounts_email": (
                    "accounts@numetricbusiness.co.ke"
                ),

                "phone": (
                    "0739 651 744"
                ),

                "office_location": (
                    "Mombasa Road, Vision Plaza"
                ),

                "website": (
                    "https://www.numetricbusiness.co.ke"
                ),

                "about_intro": (
                    "At Numetric Business Solution, we help "
                    "businesses get their numbers right and make "
                    "better informed decisions."
                ),

                "about_body": (
                    "We provide end-to-end accounting, tax, audit, "
                    "financial reporting and advisory services, "
                    "giving business owners a clear view of their "
                    "financial position and the confidence to grow.\n\n"
                    "We believe accounting should be more than "
                    "meeting tax and regulatory requirements. It "
                    "should give business leaders the insight and "
                    "control they need to manage performance, "
                    "address challenges early, and make sound "
                    "decisions.\n\n"
                    "We work alongside our clients as trusted "
                    "partners, combining professional expertise "
                    "with smarter processes and automation to "
                    "provide timely, reliable financial information.\n\n"
                    "Our approach is tailored to each client, "
                    "helping them strengthen their operations and "
                    "build stronger, more profitable businesses."
                ),

                "mission": (
                    "To provide businesses with reliable financial "
                    "expertise, practical solutions, and strategic "
                    "support that strengthen performance, manage "
                    "risk, and protect what our clients have built."
                ),

                "vision": (
                    "To create a future where every Kenyan business "
                    "achieves sustainable growth through financial "
                    "clarity, compliance certainty, and strategic "
                    "insight."
                ),

                "is_active": True,
            },
        )

        self.stdout.write(
            "  ✓ Site settings"
        )

    # ======================================================
    # SERVICES
    # ======================================================

    def seed_services(self):

        for item in self.SERVICES:

            Service.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "name": item["name"],
                    "number": item["number"],
                    "tagline": item["tagline"],
                    "overview": item["overview"],
                    "services": item["services"],
                    "who_its_for": item["who_its_for"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.SERVICES)} services"
        )

    # ======================================================
    # CATEGORIES
    # ======================================================

    def seed_categories(self):

        for item in self.CATEGORIES:

            Category.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "name": item["name"],
                    "description": item["description"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.CATEGORIES)} blog categories"
        )

    # ======================================================
    # CORE VALUES
    # ======================================================

    def seed_core_values(self):

        for item in self.CORE_VALUES:

            CoreValue.objects.update_or_create(
                number=item["number"],
                defaults={
                    "name": item["name"],
                    "description": item["description"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.CORE_VALUES)} core values"
        )

    # ======================================================
    # TESTIMONIALS
    # ======================================================

    def seed_testimonials(self):

        for item in self.TESTIMONIALS:

            Testimonial.objects.update_or_create(
                display_order=item["display_order"],
                defaults={
                    "quote": item["quote"],
                    "name": item["name"],
                    "role": item["role"],
                    "company": item["company"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.TESTIMONIALS)} testimonials"
        )

    # ======================================================
    # CERTIFICATIONS
    # ======================================================

    def seed_certifications(self):

        for item in self.CERTIFICATIONS:

            Certification.objects.update_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "display_order": item["display_order"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.CERTIFICATIONS)} certifications"
        )

    # ======================================================
    # AFFILIATIONS
    # ======================================================

    def seed_affiliations(self):

        for item in self.AFFILIATIONS:

            ProfessionalAffiliation.objects.update_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "display_order": item["display_order"],
                    "is_active": True,
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.AFFILIATIONS)} affiliations"
        )

    # ======================================================
    # BLOG POSTS
    # ======================================================

    def seed_posts(self):

        categories = {
            category.name: category
            for category in Category.objects.all()
        }

        for item in self.POSTS:

            category = categories.get(
                item["category"]
            )

            if not category:

                self.stdout.write(
                    self.style.WARNING(
                        "Skipping post because category "
                        f"was not found: {item['title']}"
                    )
                )

                continue

            Post.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "category": category,
                    "title": item["title"],
                    "excerpt": item["excerpt"],
                    "body": item["body"],
                    "author": (
                        "Numetric Business Solution"
                    ),
                    "published_at": None,
                    "is_published": False,
                    "is_featured": False,
                    "seo_title": item["title"],
                    "seo_description": item["excerpt"],
                },
            )

        self.stdout.write(
            f"  ✓ {len(self.POSTS)} blog posts"
        )