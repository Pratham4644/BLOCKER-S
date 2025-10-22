import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Mic, Send, Code2, FileText, CalendarPlus } from "lucide-react";
import { toast } from "sonner";

const Demo = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [command, setCommand] = useState("");
  const [output, setOutput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleMicClick = () => {
    setIsRecording(!isRecording);
    if (!isRecording) {
      toast.success("Voice recording started! (Demo mode)");
      setTimeout(() => {
        setIsRecording(false);
        setCommand("Analyze my binary tree code");
        toast.info("Voice command captured");
      }, 2000);
    }
  };

  const handleRunAnalysis = async () => {
    setIsLoading(true);
    setOutput("Analyzing...");
    
    setTimeout(() => {
      setOutput(`✅ Analysis Complete!\n\n🔍 Code Quality: Good\n⚡ Time Complexity: O(n log n)\n📊 Space Complexity: O(n)\n💡 Suggestion: Consider using iterative approach for better memory efficiency.\n\n✨ Your code structure is solid! Practice more tree traversal patterns.`);
      setIsLoading(false);
      toast.success("Analysis complete!");
    }, 1500);
  };

  const handleCreateNote = async () => {
    setIsLoading(true);
    setOutput("Creating Notion note...");
    
    setTimeout(() => {
      setOutput("✅ Notion Note Created!\n\n📝 Topic: Binary Search Trees\n🔗 Link: notion.so/bst-study-guide\n📅 Review Date: Tomorrow\n\n✨ Study materials and resources added automatically.");
      setIsLoading(false);
      toast.success("Note created in Notion!");
    }, 1200);
  };

  const handleScheduleTask = async () => {
    setIsLoading(true);
    setOutput("Scheduling task...");
    
    setTimeout(() => {
      setOutput("✅ Task Scheduled!\n\n📅 Google Calendar: Updated\n⏰ Reminder: 6:00 PM Today\n📧 Gmail: Confirmation sent\n💬 Slack: Team notified\n\n✨ Your learning session is all set!");
      setIsLoading(false);
      toast.success("Task scheduled across all platforms!");
    }, 1200);
  };

  return (
    <section id="demo" className="py-20 px-4 bg-gradient-card">
      <div className="container mx-auto max-w-4xl">
        <div className="text-center mb-12 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold">
            🎙️ Try Your{" "}
            <span className="bg-gradient-accent bg-clip-text text-transparent">
              AI Assistant
            </span>
          </h2>
          <p className="text-xl text-muted-foreground">
            Experience the power of voice commands and automated workflows
          </p>
        </div>

        <div className="bg-card border border-border rounded-2xl p-8 shadow-card space-y-6">
          {/* Voice/Text Input */}
          <div className="flex flex-col md:flex-row gap-4">
            <button
              onClick={handleMicClick}
              className={`flex-shrink-0 w-16 h-16 rounded-full flex items-center justify-center transition-all duration-300 ${
                isRecording
                  ? "bg-accent animate-pulse-glow"
                  : "bg-gradient-accent hover:shadow-accent-glow"
              }`}
            >
              <Mic className="text-white" size={28} />
            </button>

            <div className="flex-1 flex gap-2">
              <Input
                value={command}
                onChange={(e) => setCommand(e.target.value)}
                placeholder="Type a command or use voice..."
                className="bg-background border-border text-lg"
              />
              <Button
                onClick={handleRunAnalysis}
                disabled={!command || isLoading}
                className="bg-primary hover:bg-primary-glow"
              >
                <Send size={20} />
              </Button>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Button
              onClick={handleRunAnalysis}
              disabled={isLoading}
              className="bg-gradient-to-r from-primary to-primary-glow hover:shadow-glow"
              size="lg"
            >
              <Code2 className="mr-2" size={20} />
              Run Analysis
            </Button>
            <Button
              onClick={handleCreateNote}
              disabled={isLoading}
              className="bg-gradient-to-r from-purple-600 to-pink-600 hover:shadow-accent-glow"
              size="lg"
            >
              <FileText className="mr-2" size={20} />
              Create Notion Note
            </Button>
            <Button
              onClick={handleScheduleTask}
              disabled={isLoading}
              className="bg-gradient-to-r from-accent to-accent-glow hover:shadow-accent-glow"
              size="lg"
            >
              <CalendarPlus className="mr-2" size={20} />
              Schedule Task
            </Button>
          </div>

          {/* Output Display */}
          <div className="bg-background border border-border rounded-xl p-6 min-h-[200px]">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-2 h-2 bg-accent rounded-full animate-pulse" />
              <span className="text-sm font-semibold text-muted-foreground">Output</span>
            </div>
            <pre className="text-foreground/90 whitespace-pre-wrap font-mono text-sm">
              {output || "Ready to process your commands..."}
            </pre>
          </div>

          <p className="text-center text-xs text-muted-foreground">
            💡 Demo mode: Simulated responses. Backend integration coming soon!
          </p>
        </div>
      </div>
    </section>
  );
};

export default Demo;
