"""
Stracker Intro — 75s Sales Video
6 scenes: Hook → Logo → Dashboard → Lead-to-Deal → Billing Portal → CTA
Hybrid (now all-Manim) — 1920x1080 @ 60fps

Brand colors (from Stracker crosshairs logo):
  - Navy:    #0F1729  (background)
  - Teal:    #1AB394  (primary)
  - Orange:  #F5A623  (accent)
  - Light:   #F4F6FA  (text)
  - Muted:   #8896A8  (secondary text)
"""

from manim import *

# ==================== BRAND CONSTANTS ====================
BG      = "#0F1729"
TEAL    = "#1AB394"
ORANGE  = "#F5A623"
LIGHT   = "#F4F6FA"
MUTED   = "#8896A8"
RED     = "#E74C3C"
GREEN   = "#27AE60"
PANEL   = "#1A2540"  # slightly lighter than BG for cards

MONO = "Menlo"

# ==================== HELPERS ====================
def make_panel(width=4.5, height=1.0, color=PANEL, stroke=TEAL, stroke_width=1):
    """A rounded card panel for UI mockups."""
    return RoundedRectangle(
        width=width, height=height, corner_radius=0.1,
        fill_color=color, fill_opacity=1.0,
        stroke_color=stroke, stroke_width=stroke_width,
    )


def add_caption(scene, text, duration=None, font_size=32, color=LIGHT, position=DOWN, buff=0.5):
    """Bottom caption that doesn't need to be explicitly animated."""
    caption = Text(text, font_size=font_size, color=color, font=MONO, weight=BOLD)
    caption.to_edge(position, buff=buff)
    if duration is not None:
        scene.add_subcaption(text, duration=duration)
    return caption


# ==================== SCENE 1: HOOK ====================
class Scene1_Hook(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title (large, centered, never gets covered)
        title = Text("Sales shouldn't feel like this.", font_size=52, color=LIGHT,
                     font=MONO, weight=BOLD)
        title.move_to([0, 0.4, 0])

        # Subtitle
        subtitle = Text("Spreadsheets. Sticky notes. Group chats.", font_size=22,
                        color=MUTED, font=MONO)
        subtitle.next_to(title, DOWN, buff=0.4)

        # "Chaos" elements — all positioned in the upper third to NOT cover title
        # Spreadsheet fragment (top-left)
        sheet_group = VGroup()
        for r in range(3):
            for c in range(3):
                cell = Rectangle(
                    width=0.5, height=0.28,
                    fill_color=PANEL, fill_opacity=0.7,
                    stroke_color=MUTED, stroke_width=0.5,
                )
                cell.move_to(np.array([-5.0 + c * 0.55, 2.6 - r * 0.32, 0]))
                sheet_group.add(cell)
        x1 = Text("X", font_size=16, color=RED, font=MONO, weight=BOLD).move_to(sheet_group[2].get_center())
        x2 = Text("X", font_size=16, color=RED, font=MONO, weight=BOLD).move_to(sheet_group[7].get_center())

        # Sticky notes (top-right)
        note1 = Square(side_length=0.7, fill_color="#FFD966", fill_opacity=0.9, stroke_width=0)
        note1.rotate(0.2).move_to([4.2, 2.8, 0])
        note2 = Square(side_length=0.6, fill_color="#F6B26B", fill_opacity=0.9, stroke_width=0)
        note2.rotate(-0.15).move_to([5.2, 1.9, 0])

        # Chat bubbles with actual text
        bubble1 = RoundedRectangle(width=2.4, height=0.55, corner_radius=0.15,
                                    fill_color=TEAL, fill_opacity=0.85, stroke_width=0)
        bubble1.move_to([-3.5, -2.4, 0])
        bubble1_text = Text("did you call them?", font_size=14, color=BG, font=MONO, weight=BOLD)
        bubble1_text.move_to(bubble1.get_center())

        bubble2 = RoundedRectangle(width=2.0, height=0.55, corner_radius=0.15,
                                    fill_color=ORANGE, fill_opacity=0.85, stroke_width=0)
        bubble2.move_to([3.5, -2.4, 0])
        bubble2_text = Text("where's the quote?", font_size=14, color=BG, font=MONO, weight=BOLD)
        bubble2_text.move_to(bubble2.get_center())

        # Question marks — keep them in upper area, small enough not to hit title
        q1 = Text("?", font_size=48, color=MUTED, font=MONO, weight=BOLD).move_to([-6.0, 1.4, 0])
        q2 = Text("?", font_size=40, color=MUTED, font=MONO, weight=BOLD).move_to([6.0, 1.4, 0])

        chaos = VGroup(sheet_group, x1, x2, note1, note2,
                       bubble1, bubble1_text, bubble2, bubble2_text, q1, q2)

        # Build up chaos first
        self.add_subcaption("Sales shouldn't feel like this.", duration=7)
        self.play(FadeIn(chaos, lag_ratio=0.05, run_time=1.2))
        self.wait(0.3)

        # Title appears
        self.play(Write(title, run_time=1.2))
        self.play(FadeIn(subtitle, shift=0.2 * UP), run_time=0.6)
        self.wait(2.5)

        # Subtle shake for emphasis
        self.play(chaos.animate.shift(0.06 * RIGHT), run_time=0.08)
        self.play(chaos.animate.shift(0.12 * LEFT), run_time=0.08)
        self.play(chaos.animate.shift(0.06 * RIGHT), run_time=0.08)
        self.wait(1.5)

        # Clear
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)
        self.wait(0.3)


# ==================== SCENE 2: LOGO REVEAL ====================
class Scene2_Logo(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Use the actual Stracker logo (now transparent, teal crosshairs)
        logo = ImageMobject("stracker-logo-transparent.png")
        # Scale to ~2.2 units tall, preserving aspect
        logo.height = 2.2
        logo.move_to([0, 0.8, 0])

        # Wordmark
        wordmark = Text("Stracker", font_size=72, color=LIGHT, font=MONO, weight=BOLD)
        wordmark.move_to([0, -1.7, 0])

        tagline = Text("Sales, organized.", font_size=24, color=TEAL, font=MONO)
        tagline.next_to(wordmark, DOWN, buff=0.3)

        # Decorative teal line
        line = Line(LEFT, RIGHT, color=TEAL, stroke_width=3)
        line.set_width(4.0).next_to(wordmark, UP, buff=0.3)

        # Brand mark halo — small, just around the logo
        halo = Circle(radius=1.5, color=TEAL, stroke_width=2, fill_opacity=0)
        halo.move_to(logo.get_center())

        self.add_subcaption("Meet Stracker.", duration=5)

        # Halo pulses in
        self.play(Create(halo), run_time=0.8)
        self.play(halo.animate.set_stroke(width=4).scale(1.05), run_time=0.4)
        self.play(halo.animate.set_stroke(width=2).scale(0.98), run_time=0.4)

        # Logo fades in
        self.play(FadeIn(logo, scale=0.85), run_time=1.2)

        # Wordmark animates in
        self.play(Create(line), run_time=0.5)
        self.play(Write(wordmark, run_time=1.0))
        self.play(FadeIn(tagline, shift=0.3 * UP), run_time=0.6)
        self.wait(2.5)

        # Clear
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
        self.wait(0.2)


# ==================== SCENE 3: DASHBOARD ====================
class Scene3_Dashboard(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Section title at the very top (above topbar)
        section_title = Text("Your pipeline, in one view.", font_size=30, color=LIGHT,
                             font=MONO, weight=BOLD)
        section_title.to_edge(UP, buff=0.25)

        # Top bar
        topbar = Rectangle(width=14, height=0.5, fill_color=PANEL, fill_opacity=1, stroke_width=0)
        topbar.move_to([0, 3.05, 0])
        logo_mini = Text("▣ Stracker", font_size=16, color=TEAL, font=MONO, weight=BOLD)
        logo_mini.move_to(topbar.get_left() + RIGHT * 0.6)
        nav = Text("Dashboard  Leads  Orders  Billing", font_size=13, color=MUTED, font=MONO)
        nav.move_to(topbar.get_center() + RIGHT * 1.5)

        # KPI Cards (4 across) — compact, sit below the topbar
        kpi_data = [
            ("Active Leads", "147", TEAL, "+12 this week"),
            ("Open Orders", "$48.2K", ORANGE, "23 deals"),
            ("Visits Today", "8", GREEN, "2 pending"),
            ("MRR", "$31.5K", TEAL, "+8.4%"),
        ]
        kpi_cards = VGroup()
        for i, (label, value, accent, sub) in enumerate(kpi_data):
            card = make_panel(width=2.6, height=1.2, color=PANEL, stroke=accent, stroke_width=1.2)
            x = -4.3 + i * 2.9
            card.move_to([x, 1.95, 0])
            label_t = Text(label, font_size=12, color=MUTED, font=MONO)
            label_t.move_to(card.get_center() + UP * 0.4)
            value_t = Text(value, font_size=26, color=accent, font=MONO, weight=BOLD)
            value_t.move_to(card.get_center() + UP * 0.0)
            sub_t = Text(sub, font_size=10, color=MUTED, font=MONO)
            sub_t.move_to(card.get_center() + DOWN * 0.38)
            kpi_cards.add(VGroup(card, label_t, value_t, sub_t))

        # Chart (left, large)
        chart_panel = make_panel(width=6.8, height=2.4, color=PANEL, stroke=MUTED, stroke_width=0.8)
        chart_panel.move_to([-3.2, 0.1, 0])
        chart_title = Text("Revenue (last 6 months)", font_size=13, color=LIGHT, font=MONO, weight=BOLD)
        chart_title.move_to(chart_panel.get_center() + UP * 0.95 + LEFT * 2.3)

        # Bar chart
        axes = Axes(
            x_range=[0, 6, 1], y_range=[0, 50, 10],
            x_length=5.8, y_length=1.5,
            axis_config={"stroke_color": MUTED, "stroke_width": 1, "include_tip": False,
                         "include_ticks": False},
        ).move_to(chart_panel.get_center() + DOWN * 0.25 + LEFT * 0.1)

        bar_heights = [22, 28, 31, 35, 42, 48]
        bars = VGroup()
        for i, h in enumerate(bar_heights):
            bar = Rectangle(
                width=0.5, height=h / 50 * 1.4,
                fill_color=TEAL, fill_opacity=0.9, stroke_width=0,
            )
            x_pos = axes.c2p(i + 0.5, 0)
            bar.move_to(x_pos, DOWN)
            bars.add(bar)
        # Baseline
        baseline = Line(
            axes.c2p(0, 0), axes.c2p(6, 0),
            color=MUTED, stroke_width=1,
        )

        # Lead list (right)
        list_panel = make_panel(width=5.6, height=2.4, color=PANEL, stroke=MUTED, stroke_width=0.8)
        list_panel.move_to([3.4, 0.1, 0])
        list_title = Text("Recent Leads", font_size=13, color=LIGHT, font=MONO, weight=BOLD)
        list_title.move_to(list_panel.get_center() + UP * 0.95 + LEFT * 2.0)

        leads = [
            ("Acme Coffee", "$4,200", ORANGE),
            ("Harbor Bistro", "$8,900", TEAL),
            ("Sunrise Diner", "$1,600", MUTED),
            ("Northside Gym", "$12,400", ORANGE),
        ]
        lead_rows = VGroup()
        for i, (name, value, dot_color) in enumerate(leads):
            row_y = list_panel.get_center()[1] + 0.55 - i * 0.4
            dot = Dot(radius=0.07, color=dot_color)
            dot.move_to([list_panel.get_left()[0] + 0.25, row_y, 0])
            name_t = Text(name, font_size=13, color=LIGHT, font=MONO)
            name_t.move_to([list_panel.get_left()[0] + 0.85, row_y, 0])
            val_t = Text(value, font_size=13, color=ORANGE, font=MONO, weight=BOLD)
            val_t.move_to([list_panel.get_right()[0] - 0.7, row_y, 0])
            lead_rows.add(VGroup(dot, name_t, val_t))

        # Assemble
        self.add_subcaption("Your pipeline, in one view.", duration=12)
        self.play(Write(section_title), run_time=0.7)
        self.play(FadeIn(topbar), FadeIn(logo_mini), FadeIn(nav), run_time=0.5)

        # KPI cards animate in staggered
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in kpi_cards],
                              lag_ratio=0.12), run_time=1.5)
        self.wait(0.3)

        # Chart panel
        self.play(FadeIn(chart_panel), Write(chart_title), run_time=0.6)
        self.play(Create(axes), Create(baseline), run_time=0.6)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.08), run_time=1.0)
        self.wait(0.3)

        # Lead list
        self.play(FadeIn(list_panel), Write(list_title), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in lead_rows],
                              lag_ratio=0.1), run_time=1.0)
        self.wait(2.0)

        # Clear
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
        self.wait(0.2)


# ==================== SCENE 4: LEAD → DEAL ====================
class Scene4_Pipeline(Scene):
    def construct(self):
        self.camera.background_color = BG

        section_title = Text("From lead to closed, tracked automatically.",
                             font_size=32, color=LIGHT, font=MONO, weight=BOLD)
        section_title.to_edge(UP, buff=0.7)
        self.add_subcaption("From lead to closed, tracked automatically.", duration=12)

        # Pipeline stages
        stages = ["New Lead", "Contacted", "Visit Done", "Quoted", "Won"]
        stage_colors = [MUTED, ORANGE, TEAL, "#5DADE2", GREEN]
        n = len(stages)
        stage_width = 1.85
        gap = 0.4
        total_w = n * stage_width + (n - 1) * gap
        start_x = -total_w / 2 + stage_width / 2

        stage_boxes = VGroup()
        stage_labels = VGroup()
        for i, (s, c) in enumerate(zip(stages, stage_colors)):
            x = start_x + i * (stage_width + gap)
            box = RoundedRectangle(
                width=stage_width, height=0.55, corner_radius=0.08,
                fill_color=PANEL, fill_opacity=0.8,
                stroke_color=c, stroke_width=2,
            ).move_to([x, 2.0, 0])
            label = Text(s, font_size=16, color=c, font=MONO, weight=BOLD)
            label.move_to(box.get_center())
            stage_boxes.add(box)
            stage_labels.add(label)

        # Connecting arrows
        arrows = VGroup()
        for i in range(n - 1):
            x1 = stage_boxes[i].get_right()[0]
            x2 = stage_boxes[i + 1].get_left()[0]
            arr = Arrow(
                [x1 + 0.05, 2.0, 0], [x2 - 0.05, 2.0, 0],
                color=MUTED, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.3,
            )
            arrows.add(arr)

        # Lead card (will move along the pipeline)
        def make_lead_card(name, value, accent):
            card = RoundedRectangle(
                width=3.2, height=1.6, corner_radius=0.1,
                fill_color=PANEL, fill_opacity=1, stroke_color=accent, stroke_width=2,
            )
            name_t = Text(name, font_size=22, color=LIGHT, font=MONO, weight=BOLD)
            name_t.move_to(card.get_center() + UP * 0.4)
            val_t = Text(value, font_size=20, color=accent, font=MONO, weight=BOLD)
            val_t.move_to(card.get_center() + UP * 0.0)
            meta_t = Text("Acme Coffee Co.", font_size=13, color=MUTED, font=MONO)
            meta_t.move_to(card.get_center() + DOWN * 0.35)
            date_t = Text("Today", font_size=12, color=MUTED, font=MONO)
            date_t.move_to(card.get_center() + DOWN * 0.55)
            return VGroup(card, name_t, val_t, meta_t, date_t)

        lead_card = make_lead_card("New Lead", "Acme Coffee", ORANGE)
        lead_card.move_to([0, -0.5, 0])

        # Final "Won" card
        won_card = make_lead_card("WON ✓", "$12,400", GREEN)
        won_card.move_to([0, -0.5, 0])

        # Animations
        self.play(Write(section_title), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in stage_boxes],
                              lag_ratio=0.08), run_time=1.2)
        self.play(LaggedStart(*[Write(l) for l in stage_labels], lag_ratio=0.05), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.05), run_time=0.6)
        self.wait(0.3)

        # Card appears under first stage
        self.play(FadeIn(lead_card, shift=UP * 0.4), run_time=0.5)
        self.wait(0.4)

        # Move card across each stage, transforming color
        color_progression = [ORANGE, ORANGE, TEAL, "#5DADE2", GREEN]
        label_progression = ["New Lead", "Contacted", "Visit Done", "Quoted", "WON ✓"]
        value_progression = ["$12,400", "$12,400", "$12,400", "$12,400", "$12,400"]

        for i in range(n - 1):
            target_x = stage_boxes[i + 1].get_center()[0]
            self.play(lead_card.animate.move_to([target_x, -0.5, 0]),
                      run_time=0.6)
            # Color update
            new_card = make_lead_card(label_progression[i + 1], value_progression[i + 1],
                                      color_progression[i + 1])
            new_card.move_to([target_x, -0.5, 0])
            self.play(Transform(lead_card, new_card), run_time=0.4)
            self.wait(0.2)

        # Celebration flash on Won
        flash = Circle(radius=3.5, color=GREEN, fill_opacity=0.15, stroke_width=0)
        flash.move_to(won_card.get_center())
        self.play(FadeIn(flash), run_time=0.3)
        self.play(flash.animate.scale(1.4).set_fill(opacity=0), run_time=0.5)
        self.play(FadeOut(flash), run_time=0.3)
        self.wait(1.0)

        # Clear
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
        self.wait(0.2)


# ==================== SCENE 5: BILLING PORTAL ====================
class Scene5_Portal(Scene):
    def construct(self):
        self.camera.background_color = BG

        section_title = Text("Your customers get a clean portal too.",
                             font_size=30, color=LIGHT, font=MONO, weight=BOLD)
        section_title.to_edge(UP, buff=0.6)
        self.add_subcaption("Your customers get a clean portal too.", duration=14)

        # Portal frame
        frame = RoundedRectangle(
            width=12, height=5.2, corner_radius=0.15,
            fill_color=PANEL, fill_opacity=1, stroke_color=TEAL, stroke_width=2,
        ).move_to([0, -0.1, 0])

        # URL bar
        url_bar = RoundedRectangle(
            width=11, height=0.45, corner_radius=0.08,
            fill_color=BG, fill_opacity=1, stroke_color=MUTED, stroke_width=0.5,
        ).move_to([0, 2.0, 0])
        url_text = Text("acme-co.stracker.io", font_size=14, color=TEAL, font=MONO, weight=BOLD)
        url_text.move_to(url_bar.get_center() + LEFT * 1.2)
        # "https://" prefix and lock dot (avoid emoji which may not render)
        https_t = Text("https://", font_size=13, color=GREEN, font=MONO, weight=BOLD)
        https_t.move_to(url_bar.get_center() + LEFT * 4.5)

        # Account name
        account_name = Text("Acme Coffee Co.", font_size=26, color=LIGHT, font=MONO, weight=BOLD)
        account_name.move_to([0, 1.3, 0])

        # Three info cards
        card_data = [
            ("Account Balance", "$1,240.00", "2 invoices open"),
            ("Active Services", "4", "3 active • 1 pending"),
            ("Next Billing", "Mar 15", "Auto-charge on file"),
        ]
        info_cards = VGroup()
        for i, (label, val, sub) in enumerate(card_data):
            card = RoundedRectangle(
                width=3.3, height=1.5, corner_radius=0.1,
                fill_color=BG, fill_opacity=1, stroke_color=TEAL, stroke_width=1.2,
            )
            x = -4.0 + i * 4.0
            card.move_to([x, 0.1, 0])
            label_t = Text(label, font_size=13, color=MUTED, font=MONO)
            label_t.move_to(card.get_center() + UP * 0.45)
            val_t = Text(val, font_size=28, color=ORANGE, font=MONO, weight=BOLD)
            val_t.move_to(card.get_center() + UP * 0.0)
            sub_t = Text(sub, font_size=11, color=MUTED, font=MONO)
            sub_t.move_to(card.get_center() + DOWN * 0.45)
            info_cards.add(VGroup(card, label_t, val_t, sub_t))

        # Invoice list
        invoice_rows = VGroup()
        invoices = [
            ("INV-1042", "Feb 15, 2026", "$620.00", "Open"),
            ("INV-1031", "Jan 15, 2026", "$620.00", "Paid"),
            ("INV-1018", "Dec 15, 2025", "$580.00", "Paid"),
        ]
        for i, (num, date, amt, status) in enumerate(invoices):
            y = -1.55 - i * 0.4
            num_t = Text(num, font_size=14, color=LIGHT, font=MONO, weight=BOLD)
            num_t.move_to([-4.5, y, 0])
            date_t = Text(date, font_size=14, color=MUTED, font=MONO)
            date_t.move_to([-1.5, y, 0])
            amt_t = Text(amt, font_size=14, color=ORANGE, font=MONO, weight=BOLD)
            amt_t.move_to([1.5, y, 0])
            status_color = ORANGE if status == "Open" else GREEN
            status_t = Text(status, font_size=13, color=status_color, font=MONO, weight=BOLD)
            status_t.move_to([4.0, y, 0])
            # Row separator
            sep = Line(
                [-5.2, y - 0.2, 0], [5.2, y - 0.2, 0],
                color=MUTED, stroke_width=0.5,
            )
            invoice_rows.add(VGroup(num_t, date_t, amt_t, status_t, sep))

        # "Pay Now" button
        pay_btn = RoundedRectangle(
            width=2.2, height=0.5, corner_radius=0.08,
            fill_color=TEAL, fill_opacity=1, stroke_width=0,
        ).move_to([3.7, -0.55, 0])
        pay_text = Text("Pay Invoice", font_size=14, color=BG, font=MONO, weight=BOLD)
        pay_text.move_to(pay_btn.get_center())

        # Build up
        self.play(Write(section_title), run_time=0.7)
        self.play(FadeIn(frame), run_time=0.4)
        self.play(FadeIn(url_bar), FadeIn(url_text), FadeIn(https_t), run_time=0.4)
        self.play(Write(account_name), run_time=0.5)
        self.wait(0.2)

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in info_cards],
                              lag_ratio=0.1), run_time=1.0)
        self.wait(0.2)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in invoice_rows],
                              lag_ratio=0.1), run_time=1.0)
        self.wait(0.2)

        self.play(FadeIn(pay_btn), Write(pay_text), run_time=0.4)
        self.wait(2.5)

        # Clear
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.5)
        self.wait(0.2)


# ==================== SCENE 6: CTA ====================
class Scene6_CTA(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Logo center-top (transparent PNG, teal crosshairs)
        logo = ImageMobject("stracker-logo-transparent.png")
        logo.height = 1.8
        logo.move_to([0, 1.4, 0])

        # Wordmark
        wordmark = Text("Stracker", font_size=64, color=LIGHT, font=MONO, weight=BOLD)
        wordmark.move_to([0, -0.3, 0])

        # Tagline
        tagline = Text("Sales, organized.", font_size=28, color=TEAL, font=MONO)
        tagline.next_to(wordmark, DOWN, buff=0.4)

        # URL pill
        url_pill = RoundedRectangle(
            width=5.0, height=0.8, corner_radius=0.4,
            fill_color=TEAL, fill_opacity=1, stroke_width=0,
        ).move_to([0, -2.0, 0])
        url_text = Text("strackerapp.com", font_size=24, color=BG, font=MONO, weight=BOLD)
        url_text.move_to(url_pill.get_center())

        # Subtle ring around the logo only
        ring = Circle(radius=1.4, color=TEAL, stroke_width=1.5, fill_opacity=0)
        ring.move_to(logo.get_center())

        self.add_subcaption("strackerapp.com — Sales, organized.", duration=15)

        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(logo, scale=0.9), run_time=1.0)
        self.play(Write(wordmark, run_time=1.0))
        self.play(FadeIn(tagline, shift=0.3 * UP), run_time=0.5)
        self.play(FadeIn(url_pill, scale=0.9), Write(url_text), run_time=0.7)
        self.wait(4.0)
