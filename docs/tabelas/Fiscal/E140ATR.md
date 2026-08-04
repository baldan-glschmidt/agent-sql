# E140ATR

## Descrição

Vendas - Notas Fiscais de Saída - Atributos da Venda

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| IdcIab | Number(009,0) | Não | Índice dos benefícios do atributo de venda |
| FilPed | Number(005,0) | Sim | Código da filial |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência de item do pedido |
| DatGer | Date | Sim | Data da entrada do produto no depósito |
| HorGer | Number(005,0) | Sim | Hora da geração da requisição |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração da requisição |
| ObsAtr | String(250) | Sim | Texto da observação |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- IdcIab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
