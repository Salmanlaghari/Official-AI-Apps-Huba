import os
import re
import json
import requests
from datetime import datetime

# GitHub Config
GITHUB_OWNER = "Salmanlaghari"
BASE_URL = "https://salmanlaghari.github.io/Official-AI-Apps-Huba" # Fallback/Primary Pages URL

# 11 Applications Definition
APPS_METADATA = [
    {
        "id": "spelltype-keyboard",
        "name": "SpellType Keyboard",
        "repo": "SpellType-Keyboard",
        "category": "Productivity & Tools",
        "icon": "⌨️",
        "short_desc": "Next-gen AI-powered keyboard with advanced typo correction, real-time grammar checking, smart predictions, and glassmorphism styling.",
        "long_desc": "SpellType Keyboard is a revolutionary AI-infused typing companion for Android. It elevates your mobile communication by proofreading and polishing your text on the fly. Whether writing a professional email, crafting social media captions, or texting friends, SpellType ensures error-free, stylish, and highly articulate messages with zero lag.",
        "features": [
            "AI Grammar & Spell Check: Instantly detect and fix grammar errors, typos, and punctuation slips as you type.",
            "Tone Adjustment: Rewrite your messages to sound formal, friendly, professional, or casual with a single tap.",
            "Smart Text Prediction: Highly accurate contextual suggestions that adapt to your unique writing style.",
            "Premium Glassmorphic Themes: Gorgeous semi-transparent, neon-accented styles that match your device's aesthetics.",
            "In-built Clipboard: Quick access to snippets, pinned text, and recent copies.",
            "Privacy First: Local processing options and absolute security for personal data with zero tracking."
        ],
        "requirements": {
            "os": "Android 8.0 or higher",
            "ram": "2GB RAM (3GB recommended)",
            "storage": "50MB free space",
            "internet": "Required for online advanced AI features (offline mode available for dictionary spelling)"
        },
        "keywords": "AI Keyboard, SpellType, Grammar Correction Keyboard, Smart Android Keyboard, Auto-correction App, AI typing helper, Prince Laghari & TEAM PK AI apps"
    },
    {
        "id": "pk-ai",
        "name": "PK AI",
        "repo": "PK-AI",
        "category": "AI Assistants",
        "icon": "🇵🇰",
        "short_desc": "Pakistan's first fully-localized conversational AI assistant trained on local culture, language, laws, history, and daily utility.",
        "long_desc": "PK AI is a state-of-the-art conversational chatbot specifically tailored for Pakistan. It offers bilingual support in Urdu and English, answering questions about national history, constitution, laws, educational syllabi, and daily local updates. Experience a truly localized digital assistant that understands your culture, context, and language.",
        "features": [
            "Bilingual Conversation: Smooth chat in Urdu (both Arabic script & Roman Urdu) and English.",
            "Local Context Specialist: Expert knowledge on Pakistani culture, history, geographic regions, and heritage.",
            "Educational Helper: Get answers from national textbooks, entry test assistance, and general knowledge.",
            "Legal & Constitution Guide: Simple explainers of national regulations, citizen rights, and administrative procedures.",
            "Real-time Updates: Local weather, currency conversions, and utility computations."
        ],
        "requirements": {
            "os": "Android 7.0 or higher",
            "ram": "1.5GB RAM (2GB recommended)",
            "storage": "20MB free space",
            "internet": "Required for dynamic AI responses"
        },
        "keywords": "PK AI, Pakistan AI Assistant, Urdu chatbot, Prince Laghari & TEAM PK AI AI, local AI helper, Urdu smart chat, Pakistan digital companion"
    },
    {
        "id": "pulse-music-player-ai",
        "name": "Pulse Music Player AI",
        "repo": "Pulse-Music-Player-AI",
        "category": "Music & Audio",
        "icon": "🎵",
        "short_desc": "Intelligent offline & online music player that auto-categorizes, recommends tracks, and dynamically enhances acoustics using real-time AI filters.",
        "long_desc": "Pulse Music Player AI reinvents how you listen to music on Android. Blending a stellar neon glassmorphism layout with cutting-edge AI equalizer technology, it scans your audio library to optimize sound frequencies based on track genres. Discover dynamic lyrics, spatial audio enhancements, and automated smart playlist compilation.",
        "features": [
            "AI Equalizer (AcoustIQ): Automatically calibrates bass, treble, and vocal clarity based on active song metadata.",
            "Contextual Playlists: Auto-groups music into Moods (Focus, Gym, Calm, Sleep) using acoustic pattern detection.",
            "Floating Glass Player: Premium transparent playback controls with gorgeous real-time visualizers.",
            "Smart Lyric Sync: Searches, syncs, and embeds scrolling lyrics in real-time.",
            "Tag Auto-Fix: Uses AI-driven music registries to fix missing artist tags, album covers, and titles."
        ],
        "requirements": {
            "os": "Android 6.0 or higher",
            "ram": "1GB RAM (2GB recommended)",
            "storage": "35MB free space",
            "internet": "Optional (Required only for online streaming and lyric syncing)"
        },
        "keywords": "Pulse Music AI, AI Equalizer Android, Glassmorphism music player, Offline music player, Smart music app, music visualizer Android"
    },
    {
        "id": "rising-flix",
        "name": "Rising Flix",
        "repo": "Rising-Flix",
        "category": "Entertainment",
        "icon": "🍿",
        "short_desc": "The ultimate personalized movie, series, and anime tracking platform powered by smart recommendation engines.",
        "long_desc": "Rising Flix is a feature-rich visual tracker for cinemaphiles. Seamlessly organize your movies, TV shows, and anime in a sleek dashboard. Powered by a neural recommendation system, it analyzes your watch history to suggest hidden gems and hot new releases across streaming platforms, complete with trailers and cast specs.",
        "features": [
            "Smart Recommendations: Personalized feed of titles matched directly to your ratings and genre preferences.",
            "Multi-Platform Watchlists: Keep track of what to watch on Netflix, Disney+, Prime, and theatrical releases in one spot.",
            "Direct Trailer Player: Watch official teasers and trailers directly inside the app without ads.",
            "Chrono-Release Calendar: Never miss an upcoming episode or movie release with local reminder alerts.",
            "Detailed Cast Analytics: Explore comprehensive filmographies, fun facts, and reviews powered by community databases."
        ],
        "requirements": {
            "os": "Android 7.0 or higher",
            "ram": "2GB RAM",
            "storage": "40MB free space",
            "internet": "Required for streaming database details"
        },
        "keywords": "Rising Flix, Movie Tracker, TV Show tracker, Anime recommender, AI movie suggestions, Prince Laghari & TEAM PK AI entertainment"
    },
    {
        "id": "click-browser",
        "name": "Click Browser",
        "repo": "Click",
        "category": "Communication & Browsing",
        "icon": "🌐",
        "short_desc": "Ultra-fast, secure, and lightweight web browser with built-in ad blocker, AI page summarizer, and deep privacy safeguards.",
        "long_desc": "Click Browser is engineered for safety, speed, and intelligence. It strips out heavy trackers, banners, and redundant scripts to load websites up to 3x faster than standard browsers. With its integrated AI Summarizer, you can condense lengthy essays or news articles into clear, digestible bullets in just one click.",
        "features": [
            "AI Summarizer: Highlight or load any webpage and get an instant, intelligent summary of key takeaways.",
            "Ad-Block Extreme: Block intrusive ads, pop-ups, video sponsorships, and hidden cryptominers natively.",
            "Deep Incognito Mode: Advanced browser engine that wipes cache, cookies, and search logs on exit.",
            "Low-Data Engine: Compresses visual resources dynamically for ultra-fast browsing under poor network coverage.",
            "Sleek Glass Tabs: A fluid, futuristic navigation system that simplifies multitasking."
        ],
        "requirements": {
            "os": "Android 8.0 or higher",
            "ram": "2GB RAM (4GB recommended)",
            "storage": "45MB free space",
            "internet": "Required for browsing"
        },
        "keywords": "Click Browser, AI Browser, Fast Web Browser Android, Secure Browser, Adblocker Browser, Web Summarizer AI"
    },
    {
        "id": "ai-finder",
        "name": "AI Finder",
        "repo": "ai-finder-app",
        "category": "Productivity & Tools",
        "icon": "🔍",
        "short_desc": "Ultra-premium AI-powered search aggregator with Firebase live data, dark cyberpunk UI, and curated directory of 2000+ AI tools worldwide.",
        "long_desc": "AI Finder is an ultra-premium, AI-powered online search aggregator built with Kotlin and Jetpack Compose. It connects live to Firebase Firestore to fetch, filter, and display a curated world directory of the latest AI tools inside a beautiful dark-mode cyberpunk UI layout. Browse 2000+ AI applications across categories like Content Generation, Image Design, Coding Assistants, Voice Modulation, Video Editing, Data Analysis, and Predictive Modeling. Features include real-time search, advanced category filters, tool bookmarking, detailed tool pages with screenshots and ratings, developer API references, and daily AI news updates.",
        "features": [
            "Firebase Live Database: Real-time sync with Firestore for instant tool updates and new AI app listings.",
            "Cyberpunk Dark UI: Stunning glassmorphic design with neon accents, smooth animations, and premium dark theme.",
            "2000+ AI Tools Directory: Curated and categorized database covering every AI niche — text, image, code, voice, video, data.",
            "Advanced Search & Filters: Filter by pricing (Free/Freemium/Paid), platform, category, rating, and API availability.",
            "Tool Detail Pages: Full screenshots, feature lists, pricing info, developer links, and user ratings for each tool.",
            "Bookmark & Favorites: Save your preferred AI tools with local Room database for offline access.",
            "AI News Feed: Daily curated updates on new AI tool launches, breakthroughs, and industry trends.",
            "Developer Resources: Open-source models, training datasets, API documentation, and integration guides.",
            "Jetpack Compose UI: Modern declarative UI with Material 3, Hilt dependency injection, and MVVM architecture.",
            "Google AdMob Integration: Non-intrusive banner and interstitial ads with premium ad-free option."
        ],
        "requirements": {
            "os": "Android 7.0 (API 24) or higher",
            "ram": "1GB RAM (2GB recommended)",
            "storage": "15MB free space",
            "internet": "Required for live Firebase data sync and tool directory updates"
        },
        "keywords": "AI Finder, AI Tools Directory, Artificial Intelligence Apps, find AI software, AI models finder, Prince Laghari, TEAM PK AI, Kotlin AI app, Jetpack Compose AI, Firebase AI directory"
    },
    {
        "id": "powercut-editor",
        "name": "PowerCut Editor",
        "repo": "PowerCut-Editor",
        "category": "Video & Photo",
        "icon": "🎬",
        "short_desc": "Premium, lightweight AI-driven video editor featuring auto-scene cuts, cinematic effects, dynamic subtitles, and 4K output.",
        "long_desc": "PowerCut Editor delivers high-fidelity video processing right into your palm. Designed for social creators, its neural cutting system automatically identifies dead pauses and audio gaps in your footage, trimming them in seconds. Mix professional transitions, insert realistic text-to-speech voiceovers, and output stunning 4K projects.",
        "features": [
            "AI Smart Cut: Auto-detects silent gaps and bad frames to construct a rough cut instantly.",
            "Cinematic Transitions & Filters: Access premium glass-style blends and color correction overlays.",
            "Automated Subtitles: High-accuracy voice transcription that creates stunning, stylized captions in real-time.",
            "AI Object Eraser: Touch and remove unwanted background elements or photobombers with high-quality inpainting.",
            "Pro 4K Export: Smooth rendering engine offering custom framerates (up to 60 FPS) and zero watermark options."
        ],
        "requirements": {
            "os": "Android 9.0 or higher",
            "ram": "4GB RAM minimum (6GB+ highly recommended)",
            "storage": "200MB free space (for cache)",
            "internet": "Optional (Can be used completely offline; internet required only for asset store downloads)"
        },
        "keywords": "PowerCut Editor, AI Video Editor, Android Video Editor, Auto Cut Video, Smart Subtitle Creator, Video Trimmer app"
    },
    {
        "id": "filmhub-premium",
        "name": "FilmHub Premium",
        "repo": "FilmHub-Premium",
        "category": "Entertainment",
        "icon": "🎞️",
        "short_desc": "High-definition cataloging, global reviews, custom watchlists, and smart AI recommendations for movie lovers.",
        "long_desc": "FilmHub Premium is a bespoke digital logbook and cataloging suite built exclusively for movie enthusiasts. Enjoy an immersive interface styled with translucent elements and glowing boundaries. Catalog physical media, compose rich, markdown-supported reviews, and access premium insights on global cinema trends.",
        "features": [
            "Premium HD Cataloging: Beautifully organize your movies, series, and documentaries using custom tags and notes.",
            "Global Community Reviews: Read and write comprehensive, spoiler-controlled movie critique.",
            "AI Recommendation Engine: Analyzes local library data to suggest highly relevant watch selections.",
            "Personalized Watch Statistics: Graph your favorite directors, genres, and monthly watch hours in gorgeous charts.",
            "Offline Access: Save your personal catalogs, custom lists, and watchnotes completely offline."
        ],
        "requirements": {
            "os": "Android 8.0 or higher",
            "ram": "2GB RAM",
            "storage": "50MB free space",
            "internet": "Required for downloading movie catalogs and syncing statistics"
        },
        "keywords": "FilmHub Premium, Cinema Catalog, Movie Database organizer, Movie critiques, review cinema Android"
    },
    {
        "id": "hack-ai",
        "name": "HACK AI",
        "repo": "HACK-AI",
        "category": "Education & Tech",
        "icon": "🛡️",
        "short_desc": "Advanced cybersecurity helper offering secure code reviews, penetration testing tutorials, and vulnerability assessment guides.",
        "long_desc": "HACK AI is an ethical educational cybersecurity companion. Designed for students and penetration testers, it offers rich learning resources, safe playground guides, and interactive AI modules that examine your scripts for security vulnerabilities (e.g., OWASP Top 10) while providing remediation tips.",
        "features": [
            "AI Code Auditor: Paste snippets (Python, JS, PHP, C) to discover security flaws, SQL injections, and buffer overflows.",
            "Ethical Hacking Tutorials: Comprehensive, structured courses covering cryptography, network sniffing, and web penetration.",
            "Vulnerability Simulator: Practice analyzing sandboxed environments with interactive AI-led walkthroughs.",
            "Port & Protocol Explainer: Quickly query network ports, routing configurations, and cipher standard breakdowns.",
            "Cyber Threat Feed: Real-time global cybersecurity news, exploit publications, and patch alerts."
        ],
        "requirements": {
            "os": "Android 8.0 or higher",
            "ram": "3GB RAM (4GB recommended)",
            "storage": "30MB free space",
            "internet": "Required for AI code assessments"
        },
        "keywords": "HACK AI, cybersecurity assistant, ethical hacking tutorial, secure code auditor, penetration testing helper"
    },
    {
        "id": "medical-research",
        "name": "Medical Research",
        "repo": "Medical-Research",
        "category": "Health & Fitness",
        "icon": "🩺",
        "short_desc": "AI-powered clinical search tool, medical dictionary, and research paper helper tailored for students and healthcare professionals.",
        "long_desc": "Medical Research is an advanced clinical intelligence tool for healthcare professionals and students. Powered by structured AI models, it enables instant searches across millions of peer-reviewed journals, maps complex drug interactions, categorizes pathological symptoms, and translates heavy medical jargon into clear patient summaries.",
        "features": [
            "Journal Lookup AI: Rapidly query clinical papers, abstracts, and metadata databases (e.g., PubMed, Medline) in seconds.",
            "Interactive Medical Dictionary: Search thousands of medical conditions, procedures, anatomical structures, and equipment.",
            "Drug Interaction Checker: Cross-examine multiple pharmaceutical combinations to discover warning flags and dosage indicators.",
            "Symptom Mapping Assistant: Input clinical symptoms and analyze potential pathological correlations with confidence indices.",
            "Research Summarizer: Paste dense medical literature to extract core research methodologies, findings, and sample cohorts."
        ],
        "requirements": {
            "os": "Android 7.0 or higher",
            "ram": "2GB RAM",
            "storage": "60MB free space",
            "internet": "Required for live database querying"
        },
        "keywords": "Medical Research, clinical search engine, medical dictionary, AI medicine, PubMed lookup, pharmaceutical examiner"
    },
    {
        "id": "fliki-pro",
        "name": "Fliki Pro",
        "repo": "Fliki-Pro",
        "category": "Social & Creation",
        "icon": "⚡",
        "short_desc": "Turn simple ideas into high-quality social posts, studio-grade voiceovers, and captivating short-form videos in seconds.",
        "long_desc": "Fliki Pro is an all-in-one AI creation suite optimized for Android. Express your ideas and see them instantly transform into rich multimedia. Write script lines and let the engine render cinematic short-form video cards with stunning captions, high-fidelity AI voiceovers, and license-free background scores in moments.",
        "features": [
            "Text to Video: Input a prompt, topic, or script, and witness the AI generate illustrative video slides.",
            "Studio Voiceovers: Select from 100+ natural-sounding AI voices spanning multiple accents, dialects, and genders.",
            "Dynamic Templates: Auto-adjust resolutions for Instagram Reels, YouTube Shorts, TikTok, or widescreen formats.",
            "One-Tap Subtitles: AI voice-syncing that overlays beautiful, animated captions onto your clips.",
            "Integrated Stock Library: Gain access to millions of royalty-free stock pictures, videos, and music clips."
        ],
        "requirements": {
            "os": "Android 8.0 or higher",
            "ram": "3GB RAM (4GB recommended)",
            "storage": "80MB free space",
            "internet": "Required for cloud-based rendering"
        },
        "keywords": "Fliki Pro, Text to video AI, voiceover generator, short video creator, dynamic captioning, AI content builder"
    }
]

FAQ_DATA = [
    {
        "q": "What is the Official AI Apps Hub?",
        "a": "It is the premier digital landing and update page for all Android applications developed by Prince Laghari & TEAM PK AI, focusing on cutting-edge Glassmorphism designs and AI-infused productivity tools."
    },
    {
        "q": "Are these applications safe to download and install?",
        "a": "Yes, absolutely! All applications are open-source, built securely, and signed with developer-grade certificates. You can verify and review the full source code in their respective GitHub repositories."
    },
    {
        "q": "How can I update my installed apps?",
        "a": "The Official AI Apps Hub features auto-detection of GitHub Releases. Whenever a new stable version is pushed, this website will instantly highlight the version number, changelog, and dynamic download links for the updated APK files."
    },
    {
        "q": "Do these apps require special Android permissions?",
        "a": "Some applications (like SpellType Keyboard) require system-level input permissions to operate as a keyboard. We prioritize user privacy: no personal information is tracked, collected, or transmitted."
    },
    {
        "q": "How can I submit feature requests or report a bug?",
        "a": "Every application has a dedicated GitHub repository. You can navigate to the app's details page, click on the 'GitHub Repo' button, and submit an Issue or pull request under the repository's tracker."
    }
]

def fetch_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    try:
        response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"}, timeout=10)
        if response.status_code == 200:
            releases = response.json()
            if releases:
                return releases[0] # Return latest release object
    except Exception as e:
        print(f"Error fetching release for {repo}: {e}")
    return None

def extract_screenshots_from_body(body):
    if not body:
        return []
    # Match markdown images: ![alt](url) or <img ... src="url">
    markdown_urls = re.findall(r'!\[.*?\]\((https://github.com/user-attachments/assets/[a-f0-9\-]+)\)', body)
    html_urls = re.findall(r'<img [^>]*?src="(https://github.com/user-attachments/assets/[a-f0-9\-]+)"', body)
    # Deduplicate while preserving order
    urls = []
    for u in (markdown_urls + html_urls):
        if u not in urls:
            urls.append(u)
    return urls

def clean_body_text(body):
    if not body:
        return ""
    # Strip HTML tags or raw user-attachments to make it presentable text
    text = re.sub(r'<img [^>]*?>', '', body)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    # Remove excessive empty lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def build_app_page(app, release, screenshots):
    released_status = release is not None
    tag_name = release.get("tag_name", "Coming Soon") if released_status else "Coming Soon"
    release_name = release.get("name", "In Development") if released_status else "In Development"
    published_at = release.get("published_at", "") if released_status else ""
    changelog_html = ""

    if released_status:
        # Format Date
        try:
            dt = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
            date_str = dt.strftime("%B %d, %Y")
        except:
            date_str = published_at

        raw_body = release.get("body", "")
        cleaned_body = clean_body_text(raw_body)

        # Convert markdown list to simple html list
        list_items = []
        for line in cleaned_body.split("\n"):
            line = line.strip()
            if line.startswith("•") or line.startswith("-") or line.startswith("*"):
                content = line.lstrip("•-* ").strip()
                if content:
                    list_items.append(f"<li class='flex items-start mb-2 text-gray-300'><span class='text-cyan-400 mr-2'>•</span>{content}</li>")
            elif line:
                list_items.append(f"<p class='text-gray-300 mb-2'>{line}</p>")

        changelog_content = "".join(list_items) if list_items else "<p class='text-gray-400 italic'>No detailed changelog provided.</p>"
        changelog_html = f"""
        <div class="glass-premium p-6 rounded-2xl glow-purple mb-8">
            <h3 class="text-xl font-bold mb-4 text-white flex items-center">
                <span class="mr-2 text-purple-400">⚡</span> Latest Release Notes ({tag_name})
            </h3>
            <div class="text-sm space-y-2 text-gray-300">
                <p class="text-xs text-gray-400 mb-3">Released on: {date_str}</p>
                {changelog_content}
            </div>
        </div>
        """
        download_url = release.get("html_url", f"https://github.com/{GITHUB_OWNER}/{app['repo']}/releases")
        # Check if assets exist
        assets = release.get("assets", [])
        if assets:
            download_url = assets[0].get("browser_download_url")

        status_badge = f"<span class='px-3 py-1 text-xs rounded-full bg-green-500/20 text-green-400 border border-green-500/30 font-medium glow-text-blue'>Version {tag_name}</span>"
        download_btn_html = f"""
        <a href="{download_url}" target="_blank" class="px-8 py-4 bg-gradient-neon text-white font-bold rounded-xl text-center shadow-lg hover:scale-[1.03] active:scale-[0.98] glow-hover-blue transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-6 h-6 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Download APK (Latest Release)
        </a>
        """
    else:
        status_badge = "<span class='px-3 py-1 text-xs rounded-full bg-purple-500/20 text-purple-400 border border-purple-500/30 font-medium glow-text-purple'>Coming Soon</span>"
        download_btn_html = f"""
        <button disabled class="px-8 py-4 bg-gray-800/80 text-gray-500 font-bold rounded-xl text-center border border-gray-700 cursor-not-allowed flex items-center justify-center gap-2 w-full">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            Upcoming Application
        </button>
        """
        changelog_html = f"""
        <div class="glass-premium p-6 rounded-2xl glow-blue mb-8">
            <h3 class="text-xl font-bold mb-4 text-white flex items-center">
                <span class="mr-2 text-cyan-400">⏳</span> Development Status
            </h3>
            <p class="text-gray-300 text-sm leading-relaxed">
                This premium AI application is currently in internal testing and active development. Follow the GitHub repository to stay updated on pre-releases, milestones, and beta builds!
            </p>
        </div>
        """

    # Showcase images
    screenshots_html = ""
    if screenshots:
        screenshot_cards = "".join([f"""
            <div class="flex-none w-72 h-[480px] rounded-2xl overflow-hidden glass border border-white/10 hover:border-cyan-400/50 shadow-2xl transition-all duration-300">
                <img src="{url}" class="w-full h-full object-cover select-none" alt="{app['name']} Screenshot" loading="lazy" />
            </div>
        """ for url in screenshots])
        screenshots_html = f"""
        <div class="mb-12">
            <h3 class="text-2xl font-bold mb-6 text-white flex items-center">
                <span class="mr-2 text-cyan-400">📸</span> App Screenshots
            </h3>
            <div class="flex gap-6 overflow-x-auto pb-4 scrollbar-thin scrollbar-thumb-gray-800 scrollbar-track-transparent">
                {screenshot_cards}
            </div>
        </div>
        """

    # Feature list SVG icons
    features_html = ""
    for f in app["features"]:
        title_part, desc_part = f.split(":", 1) if ":" in f else (f, "")
        features_html += f"""
        <div class="glass p-5 rounded-xl hover:translate-y-[-2px] transition-all duration-300">
            <div class="flex items-start">
                <div class="p-2 rounded-lg bg-blue-500/10 text-cyan-400 mr-4 border border-blue-500/20">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                </div>
                <div>
                    <h4 class="font-bold text-white mb-1 text-base">{title_part.strip()}</h4>
                    <p class="text-gray-400 text-sm leading-relaxed">{desc_part.strip()}</p>
                </div>
            </div>
        </div>
        """

    keywords_meta = app["keywords"]

    # SoftwareApplication Schema JSON-LD
    schema_json = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": app["name"],
        "operatingSystem": "Android",
        "applicationCategory": app["category"],
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "description": app["short_desc"],
        "author": {
            "@type": "Person",
            "name": "Prince Laghari & TEAM PK AI",
            "url": "https://github.com/Salmanlaghari"
        }
    }
    if released_status:
        schema_json["softwareVersion"] = tag_name
        schema_json["downloadUrl"] = f"https://github.com/{GITHUB_OWNER}/{app['repo']}/releases"

    schema_script = f'<script type="application/ld+json">{json.dumps(schema_json)}</script>'

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Optimization -->
    <title>{app['name']} - Official AI Apps Hub | Prince Laghari & TEAM PK AI</title>
    <meta name="description" content="{app['short_desc']}">
    <meta name="keywords" content="{keywords_meta}">
    <meta name="author" content="Prince Laghari & TEAM PK AI">

    <!-- Open Graph (Facebook / LinkedIn) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{app['name']} - Official AI Apps Hub">
    <meta property="og:description" content="{app['short_desc']}">
    <meta property="og:url" content="{BASE_URL}/apps/{app['id']}.html">
    <meta property="og:image" content="{screenshots[0] if screenshots else BASE_URL + '/assets/images/favicon.svg'}">
    <meta property="og:site_name" content="Official AI Apps Hub">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{app['name']} - Official AI Apps Hub">
    <meta name="twitter:description" content="{app['short_desc']}">
    <meta name="twitter:image" content="{screenshots[0] if screenshots else BASE_URL + '/assets/images/favicon.svg'}">

    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#03000a">

    <!-- Tailwind CSS & Custom Styles -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="../assets/css/style.css">

    <!-- Schema Markup -->
    {schema_script}
</head>
<body class="bg-[#03000a] text-gray-200 min-h-screen flex flex-col">

    <!-- Glowing Background Decorators -->
    <div class="fixed top-[-10%] left-[-10%] w-[50vw] h-[50vw] rounded-full bg-purple-900/15 blur-[120px] pointer-events-none z-[-1] floating-blob"></div>
    <div class="fixed bottom-[-10%] right-[-10%] w-[50vw] h-[50vw] rounded-full bg-blue-900/15 blur-[120px] pointer-events-none z-[-1] floating-blob-delayed"></div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-50 glass border-b border-white/5 shadow-lg">
        <div class="container mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../index.html" class="flex items-center gap-3 group">
                <img src="../assets/images/favicon.svg" alt="AI Apps Hub Logo" class="w-10 h-10 group-hover:scale-105 transition-all duration-300">
                <div class="flex flex-col">
                    <span class="text-xl font-extrabold text-white tracking-wide group-hover:text-gradient-neon transition-all duration-300">AI APPS HUB</span>
                    <span class="text-[10px] text-gray-400 tracking-widest font-mono">PRINCE LAGHARI & TEAM PK AI</span>
                </div>
            </a>
            <nav class="flex items-center gap-6">
                <a href="../index.html" class="text-sm font-medium text-gray-300 hover:text-white transition">Home</a>
                <a href="../index.html#apps" class="text-sm font-medium text-gray-300 hover:text-white transition">Applications</a>
                <a href="../index.html#about" class="text-sm font-medium text-gray-300 hover:text-white transition">Developer</a>
                <a href="https://github.com/Salmanlaghari" target="_blank" class="px-4 py-2 text-xs rounded-lg glass border border-white/10 text-white font-medium hover:border-cyan-400/50 hover:glow-blue flex items-center gap-1.5 transition">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                    GitHub Profile
                </a>
            </nav>
        </div>
    </header>

    <!-- Main Content Grid -->
    <main class="flex-grow container mx-auto px-4 py-8 max-w-6xl">
        <!-- Breadcrumb -->
        <nav class="flex text-xs text-gray-400 mb-8" aria-label="Breadcrumb">
            <ol class="inline-flex items-center space-x-1 md:space-x-3">
                <li class="inline-flex items-center">
                    <a href="../index.html" class="inline-flex items-center hover:text-white">
                        <svg class="w-3 h-3 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
                        Hub Home
                    </a>
                </li>
                <li>
                    <div class="flex items-center">
                        <svg class="w-3 h-3 text-gray-500 mx-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
                        <span class="text-gray-500">{app['category']}</span>
                    </div>
                </li>
                <li aria-current="page">
                    <div class="flex items-center">
                        <svg class="w-3 h-3 text-gray-500 mx-1" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
                        <span class="text-gray-200 font-semibold">{app['name']}</span>
                    </div>
                </li>
            </ol>
        </nav>

        <!-- Product Hero Box -->
        <div class="glass-premium p-8 rounded-3xl mb-12 flex flex-col md:flex-row gap-8 items-center md:items-start glow-blue">
            <div class="w-28 h-28 md:w-36 md:h-36 rounded-2xl bg-gradient-neon flex items-center justify-center text-5xl md:text-6xl shadow-2xl shrink-0 select-none glow-purple">
                {app['icon']}
            </div>
            <div class="flex-grow text-center md:text-left">
                <div class="flex flex-col md:flex-row md:items-center gap-3 mb-3 justify-center md:justify-start">
                    <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight">{app['name']}</h1>
                    <div class="inline-flex justify-center md:justify-start">{status_badge}</div>
                </div>
                <p class="text-xs text-purple-400 font-semibold uppercase tracking-wider mb-4 font-mono">{app['category']}</p>
                <p class="text-gray-300 text-base md:text-lg leading-relaxed mb-6">
                    {app['long_desc']}
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
                    {download_btn_html}
                    <a href="https://github.com/Salmanlaghari/{app['repo']}" target="_blank" class="px-6 py-4 glass border border-white/10 hover:border-white/20 text-white font-bold rounded-xl text-center hover:bg-white/5 active:scale-[0.98] transition flex items-center justify-center gap-2">
                        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                        View Source Code
                    </a>
                </div>
            </div>
        </div>

        <!-- Screenshots Showcase -->
        {screenshots_html}

        <!-- Two-Column Layout (Left: Features, Right: Specs & Changelog) -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Features Column (takes 2 cols) -->
            <div class="lg:col-span-2 space-y-6">
                <h3 class="text-2xl font-bold text-white flex items-center">
                    <span class="mr-2 text-cyan-400">✨</span> Key App Features
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {features_html}
                </div>
            </div>

            <!-- Specs & Changelog Column (takes 1 col) -->
            <div class="space-y-6">
                <!-- System Requirements Card -->
                <div class="glass-premium p-6 rounded-2xl glow-blue">
                    <h3 class="text-xl font-bold mb-4 text-white flex items-center">
                        <span class="mr-2 text-cyan-400">📋</span> Requirements
                    </h3>
                    <ul class="text-sm space-y-4 text-gray-300">
                        <li class="border-b border-white/5 pb-2">
                            <span class="text-gray-400 block text-xs">Operating System</span>
                            <strong class="text-white font-medium">{app['requirements']['os']}</strong>
                        </li>
                        <li class="border-b border-white/5 pb-2">
                            <span class="text-gray-400 block text-xs">System Memory</span>
                            <strong class="text-white font-medium">{app['requirements']['ram']}</strong>
                        </li>
                        <li class="border-b border-white/5 pb-2">
                            <span class="text-gray-400 block text-xs">Storage Needed</span>
                            <strong class="text-white font-medium">{app['requirements']['storage']}</strong>
                        </li>
                        <li>
                            <span class="text-gray-400 block text-xs">Connectivity</span>
                            <strong class="text-white font-medium">{app['requirements']['internet']}</strong>
                        </li>
                    </ul>
                </div>

                <!-- Changelog Card -->
                {changelog_html}
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="mt-20 glass border-t border-white/5 py-12">
        <div class="container mx-auto px-4 max-w-6xl">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6 mb-8">
                <a href="../index.html" class="flex items-center gap-3">
                    <img src="../assets/images/favicon.svg" alt="Logo" class="w-8 h-8">
                    <span class="text-lg font-bold text-white">AI APPS HUB</span>
                </a>
                <div class="flex gap-6 text-sm text-gray-400">
                    <a href="../index.html" class="hover:text-white transition">Home</a>
                    <a href="../index.html#apps" class="hover:text-white transition">All Apps</a>
                    <a href="../index.html#about" class="hover:text-white transition">About</a>
                    <a href="https://github.com/Salmanlaghari" class="hover:text-white transition">GitHub</a>
                </div>
            </div>
            <div class="border-t border-white/5 pt-8 text-center text-xs text-gray-500">
                <p>© 2026 AI Apps Hub. Built by <a href="https://github.com/Salmanlaghari" target="_blank" class="text-gray-400 hover:text-cyan-400 transition">Prince Laghari & TEAM PK AI</a>. All Rights Reserved.</p>
                <p class="mt-2 text-[10px] text-gray-600 font-mono">Precision Crafted with Glassmorphic Aesthetics & AI Architecture.</p>
            </div>
        </div>
    </footer>

</body>
</html>
"""
    return html_content

def build_index_page(apps_with_releases):
    # Featured apps (SpellType, Click Browser, PK AI, PowerCut Editor, Pulse)
    featured_ids = ["spelltype-keyboard", "click-browser", "pk-ai", "powercut-editor", "pulse-music-player-ai"]
    featured_html_list = []
    regular_html_list = []
    latest_releases_list = []

    for app, release, screenshots in apps_with_releases:
        released_status = release is not None
        tag_name = release.get("tag_name", "Coming Soon") if released_status else "Coming Soon"

        # Download Link URL
        if released_status:
            download_url = release.get("html_url", f"https://github.com/{GITHUB_OWNER}/{app['repo']}/releases")
            assets = release.get("assets", [])
            if assets:
                download_url = assets[0].get("browser_download_url")
            badge_class = "bg-green-500/20 text-green-400 border border-green-500/30"
            badge_text = f"Version {tag_name}"
            # Add to latest releases
            dt = datetime.now()
            try:
                dt = datetime.strptime(release.get("published_at"), "%Y-%m-%dT%H:%M:%SZ")
                date_str = dt.strftime("%b %d, %Y")
            except Exception:
                date_str = "Recently"

            latest_releases_list.append((dt, f"""
            <div class="glass p-5 rounded-2xl flex items-center justify-between gap-4 border border-cyan-500/10 hover:border-cyan-500/30 shadow-md">
                <div class="flex items-center gap-4">
                    <span class="text-3xl select-none">{app['icon']}</span>
                    <div>
                        <h4 class="font-bold text-white text-base">{app['name']}</h4>
                        <p class="text-xs text-cyan-400 font-medium">Released {tag_name} • {date_str}</p>
                    </div>
                </div>
                <a href="apps/{app['id']}.html" class="px-4 py-2 text-xs font-bold rounded-lg bg-cyan-500/10 hover:bg-cyan-500 text-cyan-400 hover:text-black border border-cyan-500/20 transition duration-300">
                    Changelog
                </a>
            </div>
            """))
        else:
            download_url = f"apps/{app['id']}.html"
            badge_class = "bg-purple-500/10 text-purple-400 border border-purple-500/20"
            badge_text = "Upcoming"

        # Is Featured?
        is_featured = app["id"] in featured_ids

        app_card_html = f"""
        <div class="app-card glass p-6 rounded-3xl hover:translate-y-[-4px] flex flex-col justify-between glow-hover-blue" data-category="{app['category']}" data-name="{app['name'].lower()}" data-released="{'true' if released_status else 'false'}">
            <div>
                <!-- Header Badge -->
                <div class="flex items-center justify-between mb-5">
                    <span class="text-xs uppercase font-mono tracking-widest text-purple-400">{app['category']}</span>
                    <span class="px-2.5 py-0.5 text-[10px] rounded-full font-medium {badge_class}">{badge_text}</span>
                </div>
                <!-- App Icon & Title -->
                <div class="flex items-center gap-4 mb-4">
                    <div class="w-14 h-14 rounded-xl bg-gradient-neon flex items-center justify-center text-3xl shadow-lg shrink-0 select-none">
                        {app['icon']}
                    </div>
                    <div>
                        <h3 class="font-extrabold text-white text-lg tracking-tight leading-tight">{app['name']}</h3>
                        <p class="text-xs text-gray-400 mt-1">Repo: {app['repo']}</p>
                    </div>
                </div>
                <!-- Description -->
                <p class="text-sm text-gray-300 leading-relaxed mb-6">
                    {app['short_desc']}
                </p>
            </div>
            <!-- Action Buttons -->
            <div class="grid grid-cols-2 gap-3 pt-4 border-t border-white/5">
                <a href="apps/{app['id']}.html" class="px-3 py-2.5 text-xs text-center font-bold text-gray-300 hover:text-white glass border border-white/10 hover:border-white/20 rounded-lg transition">
                    Details & Specs
                </a>
                {"<a href='" + download_url + "' target='_blank' class='px-3 py-2.5 text-xs text-center font-bold text-black bg-gradient-neon rounded-lg glow-blue hover:scale-[1.02] transition'>Download APK</a>" if released_status else "<button disabled class='px-3 py-2.5 text-xs text-center font-bold text-gray-600 bg-gray-900 border border-gray-800 rounded-lg cursor-not-allowed'>Coming Soon</button>"}
            </div>
        </div>
        """

        if is_featured:
            featured_html_list.append(app_card_html)
        regular_html_list.append(app_card_html)

    # Sort latest releases by release date descending
    latest_releases_list.sort(key=lambda x: x[0], reverse=True)
    latest_releases_html = "".join([x[1] for x in latest_releases_list])
    if not latest_releases_html:
        latest_releases_html = "<p class='text-gray-400 italic text-center w-full py-8'>Checking for active hub updates...</p>"

    featured_apps_html = "".join(featured_html_list)
    all_apps_html = "".join(regular_html_list)

    # Categories Buttons
    categories = sorted(list(set([app["category"] for app in APPS_METADATA])))
    category_buttons_html = f"""
    <button onclick="filterCategory('All')" class="category-btn px-4 py-2 text-xs font-semibold rounded-full bg-cyan-500 text-black border border-cyan-500/30 shadow-lg glow-blue transition duration-300">
        All Applications
    </button>
    """
    for cat in categories:
        category_buttons_html += f"""
        <button onclick="filterCategory('{cat}')" class="category-btn px-4 py-2 text-xs font-semibold rounded-full glass text-gray-300 hover:text-white hover:border-cyan-400/50 transition duration-300">
            {cat}
        </button>
        """

    # Generate FAQ Accordion
    faq_html = ""
    for idx, faq in enumerate(FAQ_DATA):
        faq_html += f"""
        <div class="glass p-5 rounded-2xl glow-blue border border-white/5">
            <button class="w-full text-left flex justify-between items-center focus:outline-none" onclick="toggleFaq({idx})">
                <span class="font-bold text-white text-base pr-4">{faq['q']}</span>
                <span id="faq-icon-{idx}" class="text-cyan-400 transition-transform duration-300 transform shrink-0">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path></svg>
                </span>
            </button>
            <div id="faq-ans-{idx}" class="hidden mt-3 text-sm text-gray-300 leading-relaxed border-t border-white/5 pt-3">
                {faq['a']}
            </div>
        </div>
        """

    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Optimization -->
    <title>Official AI Apps Hub - Premium Android AI Applications | Prince Laghari & TEAM PK AI</title>
    <meta name="description" content="Discover premium, glassmorphic Android applications powered by artificial intelligence. Download latest stable APK releases directly from official GitHub builds.">
    <meta name="keywords" content="Prince Laghari & TEAM PK AI, AI Apps Hub, SpellType Keyboard, Android AI applications, PK AI, Premium glassmorphic apps, APK download hub, open source Android apps">
    <meta name="author" content="Prince Laghari & TEAM PK AI">

    <!-- Open Graph (Facebook / LinkedIn) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Official AI Apps Hub | Premium Android AI Applications">
    <meta property="og:description" content="Download state-of-the-art glassmorphic Android applications built with cutting-edge AI architecture.">
    <meta property="og:url" content="{BASE_URL}/index.html">
    <meta property="og:image" content="{BASE_URL}/assets/images/favicon.svg">
    <meta property="og:site_name" content="Official AI Apps Hub">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Official AI Apps Hub | Prince Laghari & TEAM PK AI">
    <meta name="twitter:description" content="Premium, glassmorphic Android applications powered by Artificial Intelligence.">
    <meta name="twitter:image" content="{BASE_URL}/assets/images/favicon.svg">

    <!-- Favicon & Manifest -->
    <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#03000a">

    <!-- Tailwind CSS & Custom Styles -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="bg-[#03000a] text-gray-200 min-h-screen flex flex-col scroll-smooth">

    <!-- Glowing Background Blob Decorators -->
    <div class="fixed top-[-10%] left-[-10%] w-[50vw] h-[50vw] rounded-full bg-purple-900/15 blur-[120px] pointer-events-none z-[-1] floating-blob"></div>
    <div class="fixed bottom-[-10%] right-[-10%] w-[50vw] h-[50vw] rounded-full bg-blue-900/15 blur-[120px] pointer-events-none z-[-1] floating-blob-delayed"></div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-50 glass border-b border-white/5 shadow-lg">
        <div class="container mx-auto px-4 py-4 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3 group">
                <img src="assets/images/favicon.svg" alt="Logo" class="w-10 h-10 group-hover:scale-105 transition-all duration-300">
                <div class="flex flex-col">
                    <span class="text-xl font-extrabold text-white tracking-wide group-hover:text-gradient-neon transition-all duration-300">AI APPS HUB</span>
                    <span class="text-[10px] text-gray-400 tracking-widest font-mono">PRINCE LAGHARI & TEAM PK AI</span>
                </div>
            </a>
            <nav class="hidden md:flex items-center gap-6">
                <a href="#hero" class="text-sm font-medium text-gray-300 hover:text-white transition">Home</a>
                <a href="#featured" class="text-sm font-medium text-gray-300 hover:text-white transition">Featured</a>
                <a href="#apps" class="text-sm font-medium text-gray-300 hover:text-white transition">All Apps</a>
                <a href="#faq" class="text-sm font-medium text-gray-300 hover:text-white transition">FAQ</a>
                <a href="#about" class="text-sm font-medium text-gray-300 hover:text-white transition">About</a>
                <a href="https://github.com/Salmanlaghari" target="_blank" class="px-4 py-2 text-xs rounded-lg glass border border-white/10 text-white font-medium hover:border-cyan-400/50 hover:glow-blue flex items-center gap-1.5 transition">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                    GitHub Profile
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="hero" class="container mx-auto px-4 py-16 md:py-24 text-center max-w-5xl">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass border border-cyan-400/30 text-cyan-400 font-medium text-xs mb-8 glow-blue animate-pulse">
            <span class="w-2 h-2 rounded-full bg-cyan-400"></span> Live Release Auto-Sync Enabled
        </div>
        <h1 class="text-4xl md:text-7xl font-extrabold tracking-tight mb-6 leading-none">
            Futuristic <span class="text-gradient-neon glow-text-purple">AI Android</span><br>
            Application Eco-System
        </h1>
        <p class="text-gray-300 text-lg md:text-xl max-w-2xl mx-auto leading-relaxed mb-10">
            Immerse yourself in premium glassmorphic mobile utilities powered by next-gen Artificial Intelligence. Light, responsive, and crafted with security first.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#apps" class="px-8 py-4 w-full sm:w-auto bg-gradient-neon text-black font-bold rounded-xl shadow-lg hover:scale-[1.03] active:scale-[0.98] glow-hover-blue transition-all duration-300">
                Explore All Apps
            </a>
            <a href="#about" class="px-8 py-4 w-full sm:w-auto glass border border-white/10 hover:border-white/20 text-white font-bold rounded-xl hover:bg-white/5 active:scale-[0.98] transition">
                Meet the Developer
            </a>
        </div>
    </section>

    <!-- Latest Releases & Updates Grid -->
    <section class="container mx-auto px-4 py-8 max-w-6xl">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Left Side Hero Spotlight (takes 2 cols) -->
            <div class="lg:col-span-2 glass-premium p-8 rounded-3xl flex flex-col justify-between border border-cyan-400/20 glow-blue">
                <div>
                    <span class="px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 text-xs font-semibold tracking-wider uppercase border border-cyan-500/20">Spotlight Release</span>
                    <h2 class="text-2xl md:text-4xl font-extrabold text-white mt-4 mb-3 tracking-tight">SpellType Keyboard is Live!</h2>
                    <p class="text-gray-300 text-sm md:text-base leading-relaxed mb-6">
                        Experience next-level typing on Android. Proofread grammar, optimize tones, and customize keys with high-fidelity translucent themes. Built 100% locally with cloud advanced LLM extensions.
                    </p>
                </div>
                <div class="flex flex-col sm:flex-row gap-4 items-stretch sm:items-center">
                    <a href="apps/spelltype-keyboard.html" class="px-6 py-3.5 bg-gradient-neon text-white font-bold rounded-xl text-center shadow-lg hover:scale-[1.02] active:scale-[0.98] transition duration-300">
                        View Releases & Docs
                    </a>
                    <a href="https://github.com/Salmanlaghari/SpellType-Keyboard" class="px-6 py-3.5 glass border border-white/10 text-center text-white font-semibold rounded-xl hover:bg-white/5 transition">
                        Source Code
                    </a>
                </div>
            </div>

            <!-- Right Side Feed (takes 1 col) -->
            <div class="glass-premium p-6 rounded-3xl flex flex-col border border-purple-500/20 glow-purple">
                <h3 class="text-lg font-extrabold text-white mb-4 flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-purple-500 animate-pulse"></span> App Activity Feed
                </h3>
                <div class="space-y-4 overflow-y-auto max-h-[300px] pr-2 scrollbar-thin">
                    {latest_releases_html}
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Section -->
    <section id="featured" class="container mx-auto px-4 py-16 max-w-6xl">
        <div class="text-center md:text-left mb-10">
            <h2 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight">Featured Ecosystem Utilities</h2>
            <p class="text-gray-400 mt-2 text-sm md:text-base">Curated high-performance utilities pushing the boundary of mobile AI.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featured_apps_html}
        </div>
    </section>

    <!-- Interactive Apps Directory -->
    <section id="apps" class="container mx-auto px-4 py-16 max-w-6xl">
        <!-- Section Header -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 mb-10 border-b border-white/5 pb-8">
            <div class="text-center md:text-left">
                <h2 class="text-3xl md:text-5xl font-extrabold text-white tracking-tight">Full Applications Registry</h2>
                <p class="text-gray-400 mt-2 text-sm">Use filters or active keywords search to traverse our catalog.</p>
            </div>

            <!-- Live Search Bar -->
            <div class="relative w-full md:w-80">
                <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none text-gray-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </span>
                <input type="text" id="searchInput" onkeyup="filterSearch()" placeholder="Search applications..." class="w-full pl-10 pr-4 py-3 bg-[#0c0c16]/90 border border-white/10 hover:border-cyan-400/40 focus:border-cyan-400 focus:glow-blue rounded-xl text-sm text-white placeholder-gray-500 focus:outline-none transition duration-300">
            </div>
        </div>

        <!-- Filters Grid -->
        <div class="flex flex-wrap gap-3 mb-10 justify-center md:justify-start">
            {category_buttons_html}
        </div>

        <!-- Directory Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="appsContainer">
            {all_apps_html}
        </div>
    </section>

    <!-- FAQ Accordion Section -->
    <section id="faq" class="container mx-auto px-4 py-16 max-w-4xl">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight">Frequently Asked Questions</h2>
            <p class="text-gray-400 mt-2 text-sm">Everything you need to know about the eco-system software and downloads.</p>
        </div>
        <div class="space-y-4">
            {faq_html}
        </div>
    </section>

    <!-- About & Developer Section -->
    <section id="about" class="container mx-auto px-4 py-16 max-w-5xl">
        <div class="glass-premium p-8 md:p-12 rounded-3xl glow-purple border border-purple-500/10 flex flex-col md:flex-row gap-8 items-center">
            <!-- Developer Avatar Placeholder with glow -->
            <div class="w-32 h-32 md:w-48 md:h-48 rounded-full bg-gradient-neon p-1 shrink-0 glow-purple select-none">
                <div class="w-full h-full rounded-full bg-[#03000a] flex items-center justify-center text-6xl md:text-7xl">
                    👨‍💻
                </div>
            </div>
            <div class="flex-grow text-center md:text-left">
                <span class="px-3 py-1 rounded-full bg-purple-500/10 text-purple-400 text-xs font-semibold tracking-wider uppercase border border-purple-500/20">The Visionary</span>
                <h2 class="text-3xl font-extrabold text-white tracking-tight mt-3 mb-4">Prince Laghari & TEAM PK AI</h2>
                <p class="text-gray-300 text-sm md:text-base leading-relaxed mb-6">
                    A passionate Android systems architect, building state-of-the-art consumer utilities. Specializing in highly optimized client-side AI integration, hardware-accelerated rendering, and premium minimalist translucent glassmorphic styles.
                </p>
                <div class="flex flex-wrap gap-4 justify-center md:justify-start">
                    <a href="https://github.com/Salmanlaghari" target="_blank" class="px-5 py-3 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-bold border border-white/10 hover:border-white/20 transition flex items-center gap-2">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                        GitHub Main Repo
                    </a>
                    <a href="mailto:salmanlaghari@proton.me" class="px-5 py-3 rounded-lg bg-[#00e5ff]/10 hover:bg-[#00e5ff]/20 text-[#00e5ff] text-xs font-bold border border-[#00e5ff]/20 hover:border-[#00e5ff]/30 transition flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                        Contact Developer
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="glass border-t border-white/5 py-12 mt-auto">
        <div class="container mx-auto px-4 max-w-6xl">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6 mb-8">
                <a href="index.html" class="flex items-center gap-3">
                    <img src="assets/images/favicon.svg" alt="Logo" class="w-8 h-8">
                    <span class="text-lg font-bold text-white">AI APPS HUB</span>
                </a>
                <div class="flex gap-6 text-sm text-gray-400">
                    <a href="#hero" class="hover:text-white transition">Home</a>
                    <a href="#featured" class="hover:text-white transition">Featured</a>
                    <a href="#apps" class="hover:text-white transition">All Apps</a>
                    <a href="#faq" class="hover:text-white transition">FAQ</a>
                </div>
            </div>
            <div class="border-t border-white/5 pt-8 text-center text-xs text-gray-500">
                <p>© 2026 AI Apps Hub. Built by <a href="https://github.com/Salmanlaghari" target="_blank" class="text-gray-400 hover:text-cyan-400 transition">Prince Laghari & TEAM PK AI</a>. All Rights Reserved.</p>
                <p class="mt-2 text-[10px] text-gray-600 font-mono">Precision Crafted with Glassmorphic Aesthetics & AI Architecture.</p>
            </div>
        </div>
    </footer>

    <!-- Interactive Scripts -->
    <script>
        // Search Filter Functionality
        function filterSearch() {{
            const input = document.getElementById('searchInput');
            const filter = input.value.toLowerCase();
            const container = document.getElementById('appsContainer');
            const cards = container.getElementsByClassName('app-card');

            for (let i = 0; i < cards.length; i++) {{
                const appName = cards[i].getAttribute('data-name');
                if (appName.includes(filter)) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}

        // Category Filter Functionality
        function filterCategory(cat) {{
            const container = document.getElementById('appsContainer');
            const cards = container.getElementsByClassName('app-card');

            // Highlight active button
            const buttons = document.getElementsByClassName('category-btn');
            for (let btn of buttons) {{
                if (btn.innerText.trim() === cat || (cat === 'All' && btn.innerText.includes('All'))) {{
                    btn.className = "category-btn px-4 py-2 text-xs font-semibold rounded-full bg-cyan-500 text-black border border-cyan-500/30 shadow-lg glow-blue transition duration-300";
                }} else {{
                    btn.className = "category-btn px-4 py-2 text-xs font-semibold rounded-full glass text-gray-300 hover:text-white hover:border-cyan-400/50 transition duration-300";
                }}
            }}

            for (let i = 0; i < cards.length; i++) {{
                const cardCat = cards[i].getAttribute('data-category');
                if (cat === 'All' || cardCat === cat) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}

        // FAQ Toggle Accordion Functionality
        function toggleFaq(idx) {{
            const ans = document.getElementById(`faq-ans-${{idx}}`);
            const icon = document.getElementById(`faq-icon-${{idx}}`);

            if (ans.classList.contains('hidden')) {{
                ans.classList.remove('hidden');
                icon.classList.add('rotate-180');
            }} else {{
                ans.classList.add('hidden');
                icon.classList.remove('rotate-180');
            }}
        }}
    </script>

</body>
</html>
"""
    return index_content

def main():
    print("Initiating build processing of Official AI Apps Hub...")
    apps_with_releases = []

    # Sitemap dynamic entries
    sitemap_entries = [f"{BASE_URL}/index.html"]

    for app in APPS_METADATA:
        print(f"-> Processing: {app['name']} ({app['repo']})...")
        release = fetch_latest_release(GITHUB_OWNER, app["repo"])
        screenshots = []

        if release:
            print(f"   * Latest Release Detected! tag: {release.get('tag_name')}")
            # Try to grab attachments/screenshots from body
            screenshots = extract_screenshots_from_body(release.get("body", ""))
            print(f"   * Screenshots found in body: {len(screenshots)}")
        else:
            print("   * No release detected.")

        # Compile app dedicated page content
        app_html = build_app_page(app, release, screenshots)

        # Save HTML file
        output_filepath = os.path.join("apps", f"{app['id']}.html")
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(app_html)

        apps_with_releases.append((app, release, screenshots))
        sitemap_entries.append(f"{BASE_URL}/apps/{app['id']}.html")

    # Compile index page
    index_html = build_index_page(apps_with_releases)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("-> Home index.html built successfully.")

    # Generate sitemap.xml
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for entry in sitemap_entries:
        sitemap_xml += f"""  <url>
    <loc>{entry}</loc>
    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
"""
    sitemap_xml += "</urlset>"
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("-> sitemap.xml built successfully.")

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("-> robots.txt built successfully.")
    print("All hub elements processed completely and successfully!")

if __name__ == "__main__":
    main()
