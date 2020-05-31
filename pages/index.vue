<template>
  <div>
    <banner />
    <intro />
    <slogan/>
    <adashi />
    <personal-savings />
    <loan-acquisition />
    <target-users />
  </div>
</template>
<script>
import Banner from '~/components/Banner'
import Intro from '~/components/Intro'
import Slogan from '~/components/Slogan'
import Adashi from '~/components/Adashi'
import PersonalSavings from '~/components/PersonalSavings'
import LoanAcquisition from '~/components/LoanAcquisition'
import TargetUsers from '~/components/TargetUsers'
export default {
  components: { TargetUsers, LoanAcquisition, PersonalSavings, Adashi, Slogan, Intro, Banner }
}
</script>
