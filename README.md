# patternfly-org

The PatternFly Org is the source for the official documentation for PatternFly.

## Development

Development setup requires yarn. If you do not already have yarn installed on your system, see https://yarnpkg.com/en/.

A Node version greater than 18.16.0 is also required.

### Live Reload Server

#### New server

You can install the NPM dependencies with:

    yarn install

A local development server at http://localhost:8003 can be started with:

    yarn start

### Build

The site can be built with:

    yarn build

The static assets get copied to build/patternfly-org.

If you see errors, make sure that the version of the `package.json` file in `packages/documentation-framework` matches the version of the `"@patternfly/documentation-framework"` dependency in the `package.json` file in `packages/documentation-site`.

### Deploy

When you submit a PR, previews should be automatically generated for you and uploaded as PR comments. This takes between 5-10 minutes.

When the PR is merged to main, the site is first deployed to a [staging S3 bucket.](https://staging-v6.patternfly.org)

When PatternFly does a release (currently every 3 weeks) this bucket is copied to https://patternfly.org.

### Update screenshots
To update the screenshots (these are the images that you click on to see a full-page demo):

- open a terminal and run `yarn build && yarn serve`
- in another terminal, run `yarn screenshots`

Make sure that the version of Chromium you are using is relatively recent. Version 112.0.5614.0 (Developer Build), for example, isn't compatible with the latest versions of PatternFly, and your screenshots will be off.

Browse the screenshots to make sure that nothing seems super off. For V6, you can compare to [PatternFly React V6 staging](https://patternfly-react-v6.surge.sh/) and [PatternFly Core V6 staging](https://pf6.patternfly.org/) to verify. You may need to bump PatternFly-React and Core versions if things are only off in the patternfly-org workspace.

### Old submodules

You might have a dirty file tree with old submodules and folders lying around. You can remove these with:

    git clean -dfx

### Contribute to HTML/CSS

To contribute to PatternFly's HTML/CSS core repo, refer to the [core contribution guide](https://github.com/patternfly/patternfly/blob/main/patternfly-docs/site/pages/contribution.md) and the related [guidelines](https://github.com/patternfly/patternfly/blob/main/patternfly-docs/site/pages/guidelines.md).  

### pf-docs-framework documentation

There is some historic documentation on pf-docs-framework at [packages/documentation-framework/README.md](packages/documentation-framework/README.md).