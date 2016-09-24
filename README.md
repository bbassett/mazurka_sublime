# Sublime Text 3 plugin for Mazurka

## installation

* clone to packages directory

## usage

* save file as {GET.ex|GET_test.exs|POST.ex|POST_test.exs}
* menu -> Mazurka -> {Mazurka Resource|Mazurka Test}
* or command palette -> {Mazurka Resouce|Mazurka Test}

## output

file: `my_api/web/foo/bar/GET.ex`

```
defmodule MyApi.Web.Foo.Bar.GET do
  use MyApi.Resource

  mediatype Hyper do
    action do
      %{

      }
    end
  end
end
```

file: `my_api/web/foo/bar/POST.ex`

```
defmodule MyApi.Web.Foo.Bar.POST do
  use MyApi.Resource

  mediatype Hyper do
    action do
      %{

      }
    end
  end
end
```

file: `my_api/web/foo/bar/GET_test.exs`
```
defmodule Test.MyApi.Resource.Foo.Bar.GET do
  use Test.MyApi.Resource

  test "should respond with a 200" do
    request()
  after conn ->
    conn
    |> assert_status(200)
    |> assert_json(%{"greeting" => _})
  end

  test "should respond with an affordance" do
    affordance()
  after conn ->
    conn
    |> assert_json(%{"href" => _})
  end
end
```

file: `my_api/web/foo/bar/POST_test.exs`
```
defmodule Test.MyApi.Resource.Foo.Bar.POST do
  use Test.MyApi.Resource

  test "should respond with a 200" do
    request()
  after conn ->
    conn
    |> assert_status(200)
    |> assert_json(%{"greeting" => _})
  end

  test "should respond with an affordance" do
    affordance()
  after conn ->
    conn
    |> assert_json(%{"href" => _})
  end
end
```