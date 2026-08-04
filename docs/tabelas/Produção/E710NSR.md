# E710NSR

## Descrição

Ficha - Roteiro - Narrativa da Seqüência Operacional

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRot | String(014) | Não | Código do roteiro de produção associado ao produto |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Seqüência lógica da operação no roteiro de produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| SeqNsr | Number(004,0) | Não | Número seqüencial da linha da narrativa sobre a seqüência operacional |
| CodNof | String(006) | Sim | Código da narrativa automática p/ operação (instruções de trabalho) |
| DesNsr | String(999) | Sim | Descrição técnica da seqüência operacional (descrição do processo) |
| DatAlt | Date | Não | Data de geração/alteração da seqüência |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodRot
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

### IR_E710NSR_005

**Tabela:** E710SQR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |
| SeqRot | SeqRot |
| SfxSeq | SfxSeq |

