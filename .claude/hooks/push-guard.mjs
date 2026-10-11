// Stop hook: Kaelearn always pushes. While the repo has uncommitted changes or commits the
// remote hasn't got, the turn may not end; Claude is told to commit and push first.
import { execSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const input = JSON.parse(readFileSync(0, 'utf8') || '{}');
if (input.stop_hook_active) process.exit(0); // already continuing for this hook: don't loop

const cwd = process.env.CLAUDE_PROJECT_DIR || process.cwd();
const git = (args) => execSync(`git ${args}`, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();

const todo = [];
if (git('status --porcelain')) todo.push('commit the changes (git add -A, then a clear message)');
if (git('remote')) {
  let ahead = '';
  try { ahead = git('log @{u}..HEAD --oneline'); } catch { ahead = 'no upstream'; }
  if (ahead === 'no upstream') todo.push('push and set the upstream (git push -u origin HEAD)');
  else if (ahead) todo.push('push (git push)');
}
if (todo.length) {
  process.stderr.write(`Kaelearn always pushes. Before ending the turn: ${todo.join(', then ')}.`);
  process.exit(2);
}
