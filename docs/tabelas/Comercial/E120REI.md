# E120REI

## Descrição

Vendas - Pedidos - Itens de Produto - Dados dos itens da Receita

---

## Resumo

- Campos: 23
- Chave Primária: 4 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| CodEtp | Number(004,0) | Não | Código da espécie/cultura |
| CodDpp | Number(004,0) | Não | Código da praga/problema |
| CodDia | Number(009,0) | Não | Código do diagnóstico |
| CmpDia | String(3999) | Sim | Complemento do diagnóstico |
| CodApt | Number(009,0) | Não | Código tipo de aplicação |
| CodEmb | Number(004,0) | Não | Código da embalagem |
| QtdRei | Number(014,5) | Não | Quantidade do item na receita |
| QtdDos | Number(014,5) | Não | Quantidade da dose |
| UniMed | String(003) | Sim | descontinuado |
| UniMe2 | Number(009,0) | Não | Código da unidade de medida |
| VlrCal | Number(014,5) | Sim | Calda |
| NumApl | Number(004,0) | Não | Número de aplicações |
| VlrAre | Number(014,5) | Sim | Área |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd

---

## Índices

### E120REIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodEtp
- CodDpp
- CodApt
- CodDia

### E120REIIndice2

**Tipo:** Não unico

Campos:
- CodDia

### E120REIIndice3

**Tipo:** Não unico

Campos:
- CodApt

### E120REIIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodEtp
- CodDpp
- CodDia

---

## Relacionamentos

Nenhum relacionamento cadastrado.
