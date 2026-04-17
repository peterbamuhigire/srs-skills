# Running Tests and Static Analysis

The system uses PHPUnit 11.2 for unit and integration testing, PHPStan 1.11 for static analysis, and PHP CS Fixer 3.64 for code style enforcement. All three tools are installed as `require-dev` dependencies and are available in `vendor/bin/` after running `composer install`.

All commands below are run from the project root.

## Test Execution

1. Install all development dependencies (required once after cloning, or after any change to `composer.json`):

   ```
   composer install
   ```

2. Run the full test suite:

   ```
   vendor/bin/phpunit
   ```

3. Run a specific named test suite as defined in `phpunit.xml` (for example, the Sales module tests):

   ```
   vendor/bin/phpunit --testsuite=Sales
   ```

4. Run the full suite with an HTML code coverage report written to `coverage/`:

   ```
   vendor/bin/phpunit --coverage-html coverage/
   ```

   *Coverage generation requires the `xdebug` or `pcov` PHP extension to be installed and enabled. Without one of these, PHPUnit will report that no coverage driver is available.*

## Static Analysis

5. Run PHPStan at level 8 (the project's required analysis level):

   ```
   vendor/bin/phpstan analyse --level=8
   ```

   PHPStan will report type errors, undefined variables, unreachable code, and other static defects. All reported issues must be resolved before a pull request is merged.

## Code Style

6. Check code style compliance without modifying any files (dry run):

   ```
   vendor/bin/php-cs-fixer fix --dry-run
   ```

   The dry-run output lists every file that deviates from the configured style rules. No files are modified.

7. Apply all code style fixes automatically:

   ```
   vendor/bin/php-cs-fixer fix
   ```

   Run this command before committing to ensure the diff contains only intentional logic changes. Review the list of modified files after the run to confirm no unintended changes were introduced.
