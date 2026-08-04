# E081ICA

## Descrição

Tabelas - Atributos da Venda - Itens e Valores Condicionais

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcIca | Number(009,0) | Não | Índice dos itens condicionais da condição do atributo de venda |
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| TipAtr | Number(001,0) | Sim | Indicativo do tipo do atributo |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodSer | String(014) | Sim | Código do serviço |
| CodGps | String(015) | Sim | Código do Grupo de Produto/Serviço |
| QtdVen | Number(011,2) | Sim | Quantidade base para a venda |
| VlrVen | Number(014,5) | Sim | Valor a ser utilizado na venda |
| PreBas | Number(021,10) | Sim | Valor base do produto |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(009,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsIca | String(099) | Sim | Observação do item condicional |
| CodTpr | String(004) | Sim | Código da tabela de preço do produto |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |

---

## Chave Primária

- IdcIca

---

## Índices

### E081ICA_UNIQUE

**Tipo:** Unico

Campos:
- IdcIac
- IdcIca

---

## Relacionamentos

### IR_E081ICA_001

**Tabela:** E081IAC

| Origem | Destino |
|--------|---------|
| IdcIac | IdcIac |

