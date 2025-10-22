import { useState, useEffect } from "react";
import { Menu, X } from "lucide-react";
import { Button } from "@/components/ui/button";

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const menuItems = [
    { label: "Home", href: "#home" },
    { label: "Features", href: "#features" },
    { label: "Workflow", href: "#workflow" },
    { label: "Demo", href: "#demo" },
    { label: "About", href: "#about" },
  ];

  const scrollToSection = (href: string) => {
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
      setIsMobileMenuOpen(false);
    }
  };

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? "bg-background/95 backdrop-blur-lg shadow-card" : "bg-transparent"
      }`}
    >
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16 md:h-20">
          <div className="flex items-center gap-2 text-2xl font-bold">
            <span className="text-3xl">🤖</span>
            <span className="bg-gradient-accent bg-clip-text text-transparent">
              CodeSahayak
            </span>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center gap-8">
            {menuItems.map((item) => (
              <button
                key={item.label}
                onClick={() => scrollToSection(item.href)}
                className="text-foreground/80 hover:text-foreground transition-colors relative group"
              >
                {item.label}
                <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-accent group-hover:w-full transition-all duration-300" />
              </button>
            ))}
            <Button
              onClick={() => scrollToSection("#demo")}
              className="bg-gradient-accent hover:shadow-accent-glow transition-all duration-300"
            >
              Try Demo
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden text-foreground"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {isMobileMenuOpen && (
        <div className="md:hidden bg-card/95 backdrop-blur-lg border-t border-border animate-slide-in">
          <div className="container mx-auto px-4 py-4 flex flex-col gap-4">
            {menuItems.map((item) => (
              <button
                key={item.label}
                onClick={() => scrollToSection(item.href)}
                className="text-left text-foreground/80 hover:text-foreground py-2 transition-colors"
              >
                {item.label}
              </button>
            ))}
            <Button
              onClick={() => scrollToSection("#demo")}
              className="bg-gradient-accent hover:shadow-accent-glow transition-all duration-300"
            >
              Try Demo
            </Button>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
