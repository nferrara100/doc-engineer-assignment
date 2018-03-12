require 'middleman-cli'
require 'lib/sitemap_tree'
require 'lib/data_store'

module Middleman
  module Cli

    class SearchIndexer < Thor::Group
      include Thor::Actions

      def self.exit_on_failure?
        true
      end

      namespace :algolia

      def index
        STDOUT.sync = true

        @app = ::Middleman::Application.new
        @context = @app.template_context_class.new(@app, {}, {})

        @app.extensions.add_exposed_to_context(@context)

        @app_data = DataStore.new
        @sitemap_tree = SitemapTree.new(nil)

        @app.sitemap.resources.each do |r|
          unless r.instance_of?(Middleman::Sitemap::Extensions::RedirectResource) and not r.ignored
            @sitemap_tree.add(r)
          end
        end



        Algolia.init :application_id => 'FIXME',
                     :api_key        => 'FIXME'


        index = Algolia::Index.new('docs_index')

        records = []


        @sitemap_tree.from_url('documentation').flatten.each do |elt|
          # documentation for the `resource` obj can be found here => http://www.rubydoc.info/github/middleman/middleman/Middleman/Sitemap/Resource
          resource = elt.get_val
          resource_html = resource.render(layout: 'raw')


          ##############
          #    FIXME   #
          ##############
        end

        # index.add_objects(records)

      end
      Base.register(Middleman::Cli::SearchIndexer, 'algolia', 'algolia', 'Index everything')
    end

  end
end