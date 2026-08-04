# E900NSR

## Descrição

O.P./O.S. - Narrativa da Seqüência Operacional

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção para execução da Operação |
| SfxEtr | Number(003,0) | Não | Opção do Estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Seqüência lógica da Operação no Roteiro de Produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| SeqNsr | Number(004,0) | Não | Número seqüencial da linha da narrativa sobre a seqüência operacional |
| CodNof | String(006) | Sim | Código da Narrativa automática p/ operação (Instruções de trabalho) |
| DesNsr | String(999) | Sim | Descrição técnica da seqüência operacional (descrição do processo) |
| DatAlt | Date | Não | Data de geração/alteração da seqüência |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- SeqNsr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900NSR_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

