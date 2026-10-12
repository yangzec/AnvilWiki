/**
 * Agent documentation contracts: validation commands must match executable
 * scripts and CI gates, and the progress entry must remain reachable.
 * Suite counts belong to test output rather than a second handwritten list.
 */
import { existsSync, readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, test } from 'vitest';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const agents = readFileSync(join(root, 'AGENTS.md'), 'utf8');
const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8')) as {
  scripts: Record<string, string>;
};

describe('Agent documentation entry contracts', () => {
  test('documented validation commands exist and include the CI gates', () => {
    const commands = [...agents.matchAll(/^pnpm ([\w:-]+)([^\n]*)$/gm)].map((match) =>
      `${match[1]}${match[2]}`.trim(),
    );
    expect(commands.length, 'AGENTS.md must expose validation commands').toBeGreaterThan(0);
    for (const command of commands) {
      expect(pkg.scripts, `undocumented executable: pnpm ${command}`).toHaveProperty(
        command.split(' ')[0],
      );
    }
    const gates = readFileSync(join(root, '.github/actions/gates/action.yml'), 'utf8');
    const gateCommands = [...gates.matchAll(/run: pnpm ([^\n]+)/g)].map((match) => match[1].trim());
    expect(gateCommands.length, 'CI gates must expose commands').toBeGreaterThan(0);
    for (const command of gateCommands) {
      expect(commands, `missing CI gate in AGENTS.md: pnpm ${command}`).toContain(command);
    }
  });

  test('agent links resolve and documentation routes progress to the root ROADMAP', () => {
    const links = [...agents.matchAll(/\]\(([^)]+)\)/g)].map((match) => match[1].split('#')[0]);
    expect(links).toContain('ROADMAP.md');
    expect(links).toContain('README.md');
    for (const link of links) {
      expect(existsSync(join(root, link)), `broken AGENTS.md link: ${link}`).toBe(true);
    }
    for (const [file, target] of [
      ['README.md', 'ROADMAP.md'],
      ['docs/PRD.md', '../ROADMAP.md'],
      ['docs/README.md', '../ROADMAP.md'],
      ['docs/roadmap.md', '../ROADMAP.md'],
    ]) {
      expect(
        readFileSync(join(root, file), 'utf8'),
        `${file} must link the progress source`,
      ).toContain(`](${target})`);
    }
  });
});
