# E081IAB

## Descrição

Tabelas - Atributos da Venda - Itens e Valores Condicionados (Benefícios)

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcIab | Number(009,0) | Não | Índice dos benefícios do atributo de venda |
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| TipAtr | Number(001,0) | Sim | Indicativo do tipo do atributo |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodSer | String(014) | Sim | Código do serviço |
| QtdVen | Number(011,2) | Sim | Quantidade base para a venda |
| VlrVen | Number(014,5) | Sim | Valor a ser utilizado na venda |
| PreBas | Number(021,10) | Sim | Valor base do produto |
| VlrDsc | Number(014,5) | Sim | Valor do desconto a ser concedido |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(009,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsIab | String(099) | Sim | Observação do item condicionado |
| CodTpr | String(004) | Sim | Código da tabela de preço do produto |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |

---

## Chave Primária

- IdcIab

---

## Índices

### E081IAB_UNIQUE

**Tipo:** Unico

Campos:
- IdcIac
- IdcIab

---

## Relacionamentos

Nenhum relacionamento cadastrado.
