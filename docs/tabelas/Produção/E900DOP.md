# E900DOP

## Descrição

O.P./O.S. - Defeitos de fabricação p/ Estágios

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço fabricado na O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqDop | Number(005,0) | Não | Sequência incremental (componente) ou do movimento de OP (produto final) |
| CodDft | String(004) | Não | Código do defeito de fabricação |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Sim | Derivação do Produto |
| ObsDop | String(240) | Sim | Observações adicionais sobre o defeito/falha qualidade |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Apontou o Defeito |
| DatRea | Date | Sim | Data do Apontamento |
| HorRea | Number(005,0) | Sim | Hora do Apontamento do Defeito |
| QtdRe2 | Number(014,5) | Sim | Quantidade realizada de 2ª qualidade em decorrência do defeito |
| QtdRe3 | Number(014,5) | Sim | Quantidade realizada de 3ª qualidade em decorrência do defeito |
| QtdRfg | Number(014,5) | Sim | Quantidade realizada de refugos em decorrência do defeito |
| CodAco | String(004) | Sim | Código da ação corretiva |
| CodLot | String(050) | Sim | Código Lote de Produção |
| IndPop | String(001) | Sim | Indicativo de defeito do produto da O.P./O.S. |
| QtdMnc | Number(014,5) | Sim | Quantidade de material não-conforme |
| LocDft | String(001) | Sim | Local onde o defeito foi encontrado |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqDop
- CodDft

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900DOP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900DOP_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

