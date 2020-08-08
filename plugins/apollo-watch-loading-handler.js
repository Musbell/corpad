// eslint-disable-next-line @typescript-eslint/no-unused-vars
export default (isLoading, countModifier, nuxtContext) => {
  loading += countModifier
  console.log('Global loading', loading, countModifier)
}
