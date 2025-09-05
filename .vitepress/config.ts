import { defineConfig, UserConfig } from 'vitepress'
import { withSidebar } from 'vitepress-sidebar'
import { tasklist } from '@mdit/plugin-tasklist'

const ROOT = 'notes'

// https://vitepress.dev/reference/site-config
const vitePressConfig: UserConfig = {
	srcDir: ROOT,

	title: "Andrei's brain",
	description: 'Andrei Silin personal website',
	head: [['link', { rel: 'icon', href: '/lamp.svg' }]],
	cleanUrls: true,

	themeConfig: {
		siteTitle: '@shestaya_liniya',
		socialLinks: [
			{ icon: 'github', link: 'https://github.com/shestaya-liniya' },
			{ icon: 'telegram', link: 'https://t.me/shestaya_liniya' },
		],
		search: {
			provider: 'local',
		},
		editLink: {
			pattern: 'https://github.com/shestaya-liniya/brain/edit/main/:path',
		},
	},
	lastUpdated: true,

	markdown: {
		config: md => {
			md.use(tasklist, {
				containerClass: 'custom-task-list-container',
				checkboxClass: 'custom-task-checkbox',
			})
		},
	},
}

export default defineConfig(
	withSidebar(vitePressConfig, {
		/*
		 * For detailed instructions, see the links below:
		 * https://vitepress-sidebar.cdget.com/guide/options
		 */
		//
		// ============ [ RESOLVING PATHS ] ============
		documentRootPath: ROOT,
		// scanStartPath: null,
		// resolvePath: null,
		// basePath: 'src/knowledge',
		// followSymlinks: false,
		//
		// ============ [ GROUPING ] ============
		// collapsed: true,
		collapseDepth: 2,
		// rootGroupText: 'Contents',
		// rootGroupLink: 'https://github.com/jooy2',
		// rootGroupCollapsed: false,
		//
		// ============ [ GETTING MENU TITLE ] ============
		useTitleFromFileHeading: true,
		// useTitleFromFrontmatter: true,
		// useFolderLinkFromIndexFile: false,
		useFolderTitleFromIndexFile: true,
		// frontmatterTitleFieldName: 'title',
		//
		// ============ [ GETTING MENU LINK ] ============
		// useFolderLinkFromSameNameSubFile: false,
		// useFolderLinkFromIndexFile: false,
		// folderLinkNotIncludesFileName: false,
		//
		// ============ [ INCLUDE / EXCLUDE ] ============
		// excludeByGlobPattern: ['README.md', 'folder/'],
		// excludeFilesByFrontmatterFieldName: 'exclude',
		// includeDotFiles: false,
		// includeEmptyFolder: false,
		// includeRootIndexFile: false,
		// includeFolderIndexFile: false,
		//
		// ============ [ STYLING MENU TITLE ] ============
		// hyphenToSpace: true,
		// underscoreToSpace: true,
		// capitalizeFirst: false,
		// capitalizeEachWords: false,
		// keepMarkdownSyntaxFromTitle: false,
		// removePrefixAfterOrdering: false,
		// prefixSeparator: '.',
		//
		// ============ [ SORTING ] ============
		// manualSortFileNameByPriority: ['first.md', 'second', 'third.md'],
		sortFolderTo: 'bottom',
		// sortMenusByName: false,
		// sortMenusByFileDatePrefix: false,
		// sortMenusByFrontmatterOrder: false,
		// frontmatterOrderDefaultValue: 0,
		// sortMenusByFrontmatterDate: false,
		// sortMenusOrderByDescending: false,
		// sortMenusOrderNumericallyFromTitle: false,
		// sortMenusOrderNumericallyFromLink: false,
		//
		// ============ [ MISC ] ============
		// debugPrint: false,
	}),
)
