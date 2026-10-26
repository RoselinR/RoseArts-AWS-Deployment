from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "rosearts.db"

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deployment"

# Replace these sample artworks with your own details and image filenames.
    
ARTWORKS = [
    {
        "id": "1.Blue-stillness",
        "title": "Blue Stillness",
        "image": "whaleblue.png",
        "medium": "Watercolour",
        "size": "A5",
        "price": "₹650",
        "description": "A whale glides through deep blue waters beneath shimmering rays of sunlight. This ocean-inspired painting captures a peaceful underwater moment filled with movement, depth, and wonder."
    },
    {
        "id": "2.Quiet-bloom",
        "title": "Quiet Bloom",
        "image": "daisy.jpeg",
        "medium": "Mixed media",
        "size": "A5",
        "price": "₹700",
        "description": "White daisies with sunny yellow centres bloom against a rich green background. A cheerful floral artwork that brings a touch of nature, freshness, and calm to your space."
    },
    {
        "id": "3.Cherry-blossom",
        "title": "Cherry Blossom",
        "image": "cherry.jpeg",
        "medium": "Mixed media",
        "size": "A5",
        "price": "₹700",
        "description": "Glossy red cherries stand out against soft, expressive brushstrokes. This vibrant still-life painting celebrates the beauty of everyday fruit through rich reds, delicate highlights, and painterly textures."
    },
    {
        "id": "4.Charming-eyes",
        "title": "Charming Eyes",
        "image": "Eye.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,800",
        "description": "A striking eye filled with vivid colours, expressive brushstrokes, and dramatic contrast. This bold artwork explores the beauty of colour and expression, making it an eye-catching statement piece."
    },
    {
        "id": "5.Blessed-words",
        "title": "Blessed Words",
        "image": "orange.jpeg",
        "medium": "Acrylic on paper",
        "size": "A5",
        "price": "₹650",
        "description": "Bright citrus fruits accompany the handwritten words inspired by Jeremiah 29:11. This uplifting artwork combines fruit illustration and meaningful words in a cheerful, faith-inspired composition."
    },
    {
        "id": "6.Abstract-cat",
        "title": "Abstract Cat",
        "image": "cat.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A5",
        "price": "₹750",
        "description": "A playful cat takes centre stage against a colourful arrangement of geometric shapes. Bold colours, angular forms, and contrasting patterns give this modern artwork a lively personality."
    },
    {
        "id": "7.Simple-life",
        "title": "Simple Life",
        "image": "capsicum.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A5",
        "price": "₹700",
        "description": "A vibrant arrangement of red, yellow, and green capsicums celebrates the beauty of everyday ingredients. Rich colours and expressive highlights turn a familiar subject into a lively still-life painting."
    },
    {
        "id": "8.African-women",
        "title": "African Women",
        "image": "africanwomen.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,600",
        "description": "Three graceful figures are portrayed in flowing dresses of red, yellow, and blue. Expressive silhouettes and vibrant colours create a composition celebrating movement, individuality, and togetherness."
    },
    {
        "id": "9.the-Door",
        "title": "The Door",
        "image": "Door.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,800",
        "description": "A colourful doorway framed by textured brickwork and blooming flowers creates a welcoming scene. Warm architectural details and lively garden colours evoke the charm of a quiet, sunlit place."
    },
    {
        "id": "10.simple-pot",
        "title": "Simple Pot",
        "image": "pot.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,600",
        "description": "A blue-green vase filled with grapes sits beside bright yellow lemons. Rich shadows and vivid colours bring depth to this classic still-life composition, celebrating the beauty of ordinary objects."
    },
    {
        "id": "11.fruits",
        "title": "Fruits",
        "image": "fruits.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,700",
        "description": "A colourful collection of fresh fruits fills the canvas with bold reds, sunny yellows, and rich greens. Expressive brushwork and contrasting colours create an energetic celebration of nature's abundance."
    },
    {
        "id": "12.spiral3d",
        "title": "Spiral 3D",
        "image": "spiral3d.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,500",
        "description": "An intricate arrangement of black-and-white circular spirals creates a striking optical effect. Repeated lines and carefully layered patterns give the artwork a sense of rhythm, texture, and three-dimensional depth."
    },
    {
        "id": "13.elephant",
        "title": "Elephant",
        "image": "elephant.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,800",
        "description": "An affectionate elephant family is brought to life with expressive details and a soft, colourful background. This heartwarming painting celebrates family bonds, tenderness, and the gentle charm of wildlife."
    },
    {
        "id": "14.paris",
        "title": "Paris",
        "image": "paris.jpeg",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,600",
        "description": "The Eiffel Tower rises above a Parisian scene rendered in expressive black, white, and red. Contrasting tones and bold splashes of colour give this cityscape a distinctive, artistic character."
    },
    {
        "id": "15.Pear",
        "title": "Pear",
        "image": "pear.png",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,600",
        "description": "A ripe pear rests against a cool blue background, accompanied by flowing teal fabric. Carefully observed highlights, shadows, and rich textures create a classic still-life study."
    },
    {
        "id": "16.Still life apple",
        "title": "Still Life Apple",
        "image": "apple still life.png",
        "medium": "Acrylic on canvas",
        "size": "A3",
        "price": "₹1,600",
        "description": "Red and green apples rest on a draped surface, brought to life with bright highlights and rich shadows. This traditional still-life painting explores form, colour, and the interplay of light."
    }

        
]


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS enquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                artwork_id TEXT,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.context_processor
def inject_brand_links():
    return {
        "instagram_url": "https://www.instagram.com/__rose2005/",
        "brand_name": "RoseArts",
    }


@app.route("/")
def home():
    return render_template("index.html", featured=ARTWORKS[:3])


@app.route("/artwork")
def artwork_gallery():
    return render_template("artwork.html", artworks=ARTWORKS)


@app.route("/artwork/<artwork_id>")
def artwork_detail(artwork_id):
    artwork = next((a for a in ARTWORKS if a["id"] == artwork_id), None)
    if artwork is None:
        return render_template("404.html"), 404
    return render_template("detail.html", artwork=artwork)


@app.route("/enquiry", methods=["GET", "POST"])
def enquiry():
    selected_artwork = request.args.get("artwork", "")
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        artwork_id = request.form.get("artwork_id", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please complete your name, email, and message.", "error")
            return render_template(
                "enquiry.html",
                artworks=ARTWORKS,
                selected_artwork=artwork_id,
                form_data=request.form,
            ), 400

        valid_ids = {a["id"] for a in ARTWORKS}
        if artwork_id and artwork_id not in valid_ids:
            artwork_id = ""

        with get_db() as conn:
            conn.execute(
                "INSERT INTO enquiries (name, email, artwork_id, message) VALUES (?, ?, ?, ?)",
                (name, email, artwork_id, message),
            )

        flash("Thank you! Your enquiry has been saved. We will be in touch soon.", "success")
        return redirect(url_for("enquiry"))

    return render_template(
        "enquiry.html",
        artworks=ARTWORKS,
        selected_artwork=selected_artwork,
        form_data={},
    )


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


init_db()

if __name__ == "__main__":
    app.run(debug=True)
