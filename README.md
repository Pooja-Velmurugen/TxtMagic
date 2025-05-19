# ✨ TxtMagic

**TxtMagic** is a Python package that brings Magic✨ to your text! Transform ordinary text into:  
🎨 **Colorful** masterpieces | 😊 **Emoji-powered** messages | ✒️ **Stylized** fonts | 🎬 **Animated** wonders 

## 🌟 Features


### 🎨 **Colorify**
- Basic ANSI colors 
- Custom RGB colors (24-bit)
- Rainbow gradients 🌈
- Background coloring

### 😊 **Emojify**
- Smart keyword → emoji replacement
- Sentiment analysis emojis (😊/😞)
- Combine with colors and animations

### ✒️ **Fontify**
- Multiple font styles:
  - Bold, italic, underline
  - Script, fraktur, cursive
  - Subscript/superscript and more!
  - Blockfonts(Standard, bubble, shadow, minimal, outline)

### 🎬 **Animations**
- 10+ built-in effects:
  - Typing simulation
  - Glitch effect
  - Wave motion
  - Neon glow
  - 3D text
  - And more!


## 📦 Installation

```bash
pip install TxtMagic
```
## 🧪 Try It Out!

<b>Explore these ready-to-run examples to see TxtMagic in action:</b>

### 📂 Example Code

<img src="examples/Screenshot 2025-03-29 202907.png" alt="Logo" width="600"/>
</br>

### 🔮 Output

<img src="examples/Screenshot 2025-03-29 202846.png" alt="Logo" width="500"/>

### 💡Check out <a href="examples/example.py">sample program</a> for more details!


## 🔍 Feature Comparison


<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>TxtMagic</th>
      <th>Existing Packages (e.g., <code>colorama</code>, <code>emoji</code>, <code>pyfiglet</code>)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Colorization</strong></td>
      <td>✅ Supports basic colors, custom RGB, and rainbow gradients.</td>
      <td>❌ Most packages (e.g., <code>colorama</code>, <code>termcolor</code>) only support basic ANSI colors.</td>
    </tr>
    <tr>
      <td><strong>Emoji Replacement</strong></td>
      <td>✅ Replaces keywords with emojis and integrates with color and font styling.</td>
      <td>❌ Packages like <code>emoji</code> only focus on emoji replacement.</td>
    </tr>
    <tr>
      <td><strong>Font Styling</strong></td>
      <td>✅ Offers a wide range of font styles (e.g., bold, cursive, subscript, etc.).</td>
      <td>❌ Packages like <code>pyfiglet</code> focus on ASCII art, not Unicode-based font styling.</td>
    </tr>
    <tr>
      <td><strong>Text Animations</strong></td>
      <td>✅9+ built-in animations (typing, glitch, wave, gradient, neon, etc.).</td>
      <td>❌No standard package offers text animations. Requires manual implementation or external libraries like <code>curses</code>.</td>
    </tr>
    <tr>
      <td><strong>Combination of Features</strong></td>
      <td>✅  Seamlessly combines color + emojis + fonts + animations.</td>
      <td>❌ No existing package combines all four features.</td>
    </tr>
    <tr>
      <td><strong>Ease of Use</strong></td>
      <td>✅ Simple syntax for all features (e.g., wave_effect("Hello")).</td>
      <td>❌ Users must combine multiple packages and write custom code for animations.</td>
    </tr>
    <tr>
      <td><strong>Terminal Compatibility</strong></td>
      <td>✅ Works in VS Code, PyCharm, modern terminals (Windows Terminal, iTerm2).</td>
      <td>⚠️ Some packages (e.g., rich) have limited support in Jupyter/Spyder.</td>
    </tr>
    <tr>
      <td><strong>Customization</strong></td>
      <td>✅ Allows custom RGB colors, animations, emoji and unique font styles.</td>
      <td>❌ Limited customization options in most packages.</td>
    </tr>
  </tbody>
</table>

## 📜 Version History

### Version 0.1.0

<li>Font styles bold, italic, cursive, script, fraktur and more.</li> 
<li>text to emoji</li>
<li>text color, Rgb colors, log msg, background color and rainbow gradients</li>

### Version 0.1.1

<li>Emoji with the text</li>
<li>analyze sentiment emoji</li>
<li>Animations(blinking_text, typing_animation,text_shadow, text_gradient and more)</li> 

### Version 0.1.2

<li>Initial release of blockfont() with standard ASCII styles</li>
<li>Supported styles: standard, outline, bubble, shadow, minimal</li>

### Version 0.1.3 & Version 0.1.4

<li>integrated with pyfiglet font styles.</li>
<li>custom font styles: serif, sans-serif, dotmatrix, standard, outline, bubble, shadow, minimal.</li>

### Version 0.1.5

<li>fix fontify -> blockfont() text wrapping issue for the long text.</li>
<li>Long text input now automatically wraps to the next line without breaking ASCII formatting or overflowing the terminal.</li>

## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## 📄 License
MIT License -See the <a href="LICENSE">LICENSE</a> file for details.

