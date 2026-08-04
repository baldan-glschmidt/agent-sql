# E070ECN

## Descrição

Cadastros - Empresas - Definições das consistências habilitadas para a empresa

---

## Resumo

- Campos: 29
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| MnfCip | String(001) | Sim | Permite componente/subproduto igual ao produto/serviço produzido |
| MnfAdm | String(001) | Sim | Permite alterar dados do modelo de produtos/serviços que tenham OP |
| MnfRie | String(001) | Sim | Permite estágios/operações internos e externos no mesmo roteiro ou OP |
| MnfRme | String(001) | Sim | Permite múltiplos estágios/operações externos no mesmo roteiro ou OP |
| MnfDvm | String(001) | Sim | Permite informar data de validade nos componentes/subprodutos do modelo |
| MnfBag | String(001) | Sim | Permite habilitar a baixa agrupada de componentes na OP |
| CadOcf | String(001) | Sim | Permite não informar a classificação fiscal de produtos |
| MnfAmp | String(001) | Sim | Permite alterar o modelo de um produto/serviço que tenha OP |
| EstNgd | String(001) | Sim | Permite habilitar o estoque negativo em depósito |
| MnfFdf | String(001) | Sim | Permite definir filial de produção diferente entre estágios de roteiro ou OP |
| MnfAlr | String(001) | Sim | Permite alterar o lote técnico do roteiro de produtos que tenham OP |
| MnfArp | String(001) | Sim | Permite alterar o roteiro de um produto que tenha OP |
| CadMip | String(001) | Sim | Permite que produtos manufaturados para impostos não sejam do tipo produzido |
| MnfAte | String(001) | Sim | Permite alterar o tipo do estágio de um estágio já associado a uma operação |
| MnfCap | String(001) | Sim | Permite a OP produzir antes de baixar algum componente |
| MnfPif | String(001) | Sim | Permite a OP produzir após integrada ao SPED como finalizada |
| MnfDof | String(001) | Sim | Permite a OP produzir ou baixar componente em depósito de outra filial |
| MnfEcd | String(001) | Sim | Permite estornar componente de OP em data diferente da baixa |
| MnfEpd | String(001) | Sim | Permite estornar produção de OP em data diferente da entrada |
| MnfCoi | String(001) | Sim | Permite cancelar OP já integrada ao SPED |
| EstRis | String(001) | Sim | Permite reabrir período do estoque mesmo quando houver integração com SPED |
| EstRca | String(001) | Sim | Permite reabrir estoque com CAT83/09 fechada |
| EstTpt | String(001) | Sim | Permite transferência de estoque entre produtos de qualquer tipo |
| EstTqt | String(001) | Sim | Permite transferência de estoque entre qualquer quantidade |
| NfiLrr | String(001) | Sim | Permite gerar NF de retorno de industrialização não ligada à NF de remessa |
| EstCom | String(001) | Sim | Permite o cancelamento da OP sem estornar componentes baixados |
| ForFim | String(001) | Sim | Permitir Forçar Fim em OPs que não possuam entrada no estoque de prod. produzido |
| IncPro | String(001) | Sim | Permite a incorporação do mesmo produto já incluído na OP |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
