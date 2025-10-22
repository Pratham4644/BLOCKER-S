import { Github, FileText, Calendar, Mail, MessageSquare, Phone, ArrowRight } from "lucide-react";

const Workflow = () => {
  const tools = [
    { icon: Github, name: "GitHub", color: "from-gray-700 to-gray-900" },
    { icon: FileText, name: "Code Analysis", color: "from-primary to-primary-glow" },
    { icon: FileText, name: "Notion", color: "from-gray-800 to-gray-600" },
    { icon: Calendar, name: "Calendar", color: "from-blue-600 to-blue-800" },
    { icon: Mail, name: "Gmail", color: "from-red-500 to-red-700" },
    { icon: MessageSquare, name: "Slack", color: "from-purple-500 to-purple-700" },
    { icon: Phone, name: "WhatsApp", color: "from-green-500 to-green-700" },
  ];

  return (
    <section id="workflow" className="py-20 px-4">
      <div className="container mx-auto">
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold">
            Automated{" "}
            <span className="bg-gradient-accent bg-clip-text text-transparent">
              Workflow
            </span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            One command triggers multiple actions across all your tools
          </p>
        </div>

        {/* Desktop Workflow */}
        <div className="hidden md:flex items-center justify-center gap-4 mb-12">
          {tools.map((tool, index) => {
            const Icon = tool.icon;
            return (
              <div key={tool.name} className="flex items-center gap-4">
                <div
                  className="group relative"
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <div
                    className={`w-20 h-20 rounded-2xl bg-gradient-to-br ${tool.color} flex items-center justify-center shadow-card hover:shadow-glow transition-all duration-300 hover:scale-110 cursor-pointer animate-fade-in`}
                  >
                    <Icon className="text-white" size={32} />
                  </div>
                  <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 text-xs text-center text-muted-foreground opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
                    {tool.name}
                  </div>
                </div>
                {index < tools.length - 1 && (
                  <ArrowRight className="text-primary animate-pulse" size={24} />
                )}
              </div>
            );
          })}
        </div>

        {/* Mobile Workflow */}
        <div className="md:hidden grid grid-cols-2 gap-6 max-w-md mx-auto">
          {tools.map((tool, index) => {
            const Icon = tool.icon;
            return (
              <div
                key={tool.name}
                className={`bg-gradient-to-br ${tool.color} rounded-2xl p-6 flex flex-col items-center gap-3 shadow-card hover:shadow-glow transition-all duration-300 hover:scale-105 animate-fade-in`}
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <Icon className="text-white" size={32} />
                <span className="text-white text-sm font-medium">{tool.name}</span>
              </div>
            );
          })}
        </div>

        {/* Process Description */}
        <div className="mt-16 max-w-3xl mx-auto bg-gradient-card border border-border rounded-2xl p-8">
          <h3 className="text-2xl font-bold mb-6 text-center">How It Works</h3>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="space-y-2">
              <div className="text-4xl font-bold text-primary">01</div>
              <h4 className="font-semibold">Voice/Text Command</h4>
              <p className="text-sm text-muted-foreground">
                Speak or type your request in Marathi or English
              </p>
            </div>
            <div className="space-y-2">
              <div className="text-4xl font-bold text-accent">02</div>
              <h4 className="font-semibold">AI Processing</h4>
              <p className="text-sm text-muted-foreground">
                LangChain + Composio orchestrate the workflow
              </p>
            </div>
            <div className="space-y-2">
              <div className="text-4xl font-bold text-primary-glow">03</div>
              <h4 className="font-semibold">Multi-Tool Execution</h4>
              <p className="text-sm text-muted-foreground">
                All platforms updated automatically in seconds
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Workflow;
