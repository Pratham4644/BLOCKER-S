import { Github, Linkedin, Youtube, Heart } from "lucide-react";

const Footer = () => {
  const socialLinks = [
    { icon: Github, href: "https://github.com", label: "GitHub" },
    { icon: Linkedin, href: "https://linkedin.com", label: "LinkedIn" },
    { icon: Youtube, href: "https://youtube.com", label: "YouTube" },
  ];

  return (
    <footer className="bg-card border-t border-border py-12 px-4">
      <div className="container mx-auto">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          {/* Logo & Copyright */}
          <div className="flex flex-col items-center md:items-start gap-2">
            <div className="flex items-center gap-2 text-xl font-bold">
              <span className="text-2xl">🤖</span>
              <span className="bg-gradient-accent bg-clip-text text-transparent">
                CodeSahayak
              </span>
            </div>
            <p className="text-sm text-muted-foreground flex items-center gap-1">
              © 2025 CodeSahayak | Built with <Heart className="text-red-500 inline" size={14} /> by{" "}
              <span className="text-primary font-semibold">Prathamesh Shinde</span>
            </p>
          </div>

          {/* Social Links */}
          <div className="flex gap-4">
            {socialLinks.map((social) => {
              const Icon = social.icon;
              return (
                <a
                  key={social.label}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-full bg-muted hover:bg-primary/20 flex items-center justify-center transition-all duration-300 hover:scale-110 hover:shadow-glow group"
                  aria-label={social.label}
                >
                  <Icon className="text-muted-foreground group-hover:text-primary transition-colors" size={20} />
                </a>
              );
            })}
          </div>
        </div>

        {/* Additional Links */}
        <div className="mt-8 pt-8 border-t border-border text-center">
          <p className="text-xs text-muted-foreground">
            Made for empowering CS students across India 🇮🇳 | Bilingual AI Mentor for DSA Learning
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
