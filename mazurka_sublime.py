import sublime, sublime_plugin, re

class ResourceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    allcontent = sublime.Region(0, self.view.size())

    filePath = self.view.file_name()
    if filePath:
      pathArray = str.split(filePath, '/')
      webIndex = pathArray.index('web')
      routeArray = pathArray[webIndex - 1:]
      newRouteArray = list()
      apiName = ''
      for i, part in enumerate(routeArray):
        if part.find('.ex') != -1:
          part = part.replace('.ex', '').upper()
        else: part = part.title()

        partList = re.split(r"_|-", part)
        if len(partList) > 1:
          part = ''.join(e.title() for e in partList)

        if part == 'web': part = 'resource'

        if part.find('@') != -1:
          part = str.split(part, '@')[1] + '_'

        if i == 0: apiName = part

        newRouteArray.append(part)

      resourceName = str.join('.', newRouteArray)

      module = 'defmodule ' + resourceName + ' do\n  use ' + apiName + '.Resource\n\n  mediatype Hyper do\n    action do\n      %{\n\n      }\n    end\n  end\nend'
      self.view.replace(edit, allcontent, module);
    else:
      sublime.error_message('File must be saved first')

class TestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    allcontent = sublime.Region(0, self.view.size())

    filePath = self.view.file_name()
    if filePath:
      pathArray = str.split(filePath, '/')
      webIndex = pathArray.index('web')
      routeArray = pathArray[webIndex - 1:]
      newRouteArray = list()
      apiName = ''
      for i, part in enumerate(routeArray):
        if part.find('_test.exs'): part = part.replace('_test.exs', '').upper()
        elif part.find('.ex') != -1: part = part.replace('.ex', '').upper()
        else: part = part.title()

        partList = re.split(r"_|-", part)
        if len(partList) > 1:
          part = ''.join(e.title() for e in partList)

        if part.lower() == 'web': part = 'Resource'

        if part.find('@') != -1:
          part = str.split(part, '@')[1] + '_'

        if i == 0: apiName = part

        newRouteArray.append(part)

      print(newRouteArray)

      resourceName = str.join('.', newRouteArray)

      module = 'defmodule Test.' + resourceName + ' do\n  use Test.' + apiName + '.Resource\n\n  test "should respond with a 200" do\n    request()\n  after conn ->\n    conn\n    |> assert_status(200)\n    |> assert_json(%{"greeting" => _})\n  end\n\n  test "should respond with an affordance" do\n    affordance()\n  after conn ->\n    conn\n    |> assert_json(%{"href" => _})\n  end\nend\n'
      self.view.replace(edit, allcontent, module);
    else:
      sublime.error_message('File must be saved first')