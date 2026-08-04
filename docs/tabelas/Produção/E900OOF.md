# E900OOF

## Descrição

O.P./O.S. - Ferramentas/Equipamentos previstos para utilização na operação

---

## Resumo

- Campos: 18
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção para execução da Operação |
| SfxEtr | Number(003,0) | Não | Opção do Estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Sequência lógica da Operação no Roteiro de Produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| CodFrt | String(014) | Não | Código da Ferramenta |
| DerFrt | String(007) | Não | Código da derivação da Ferramenta |
| SeqOof | Number(004,0) | Não | Seq. Ferramentas/Equipamentos previstos para utilização na operação |
| NumSep | String(050) | Sim | Série de fabricação ligada a ferramenta |
| CodEqp | String(020) | Sim | Código do equipamento ligado a ferramenta/série |
| QtdFrt | Number(004,0) | Não | Quantidade de ferramentas necessárias |
| MovFrt | String(001) | Sim | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| SolFrt | String(001) | Sim | Indica se a ferramenta/equipamento foi solicitado/atendido no Estoque |
| CodCre | String(008) | Sim | Código do Centro de Recurso onde a ferramenta será executada |
| CodDep | String(010) | Sim | Código do depósito da ferramenta |
| CodCcu | String(009) | Sim | Código do Centro de Custo. |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- CodFrt
- DerFrt
- SeqOof

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900OOF_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900OOF_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

