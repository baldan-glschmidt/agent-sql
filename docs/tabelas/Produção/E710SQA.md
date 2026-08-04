# E710SQA

## Descrição

Ficha - Roteiro - Acessório para Seqüência Operacional

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
| CodAcs | String(008) | Não | Código do acessório na seqüência operacional do processo |
| QtdAcs | Number(009,0) | Não | Quantidade de acessórios utilizados na seqüência operacional |
| ObsAcs | String(240) | Sim | Observações adicionais sobre o acessório na seqüência operacional |
| DatAlt | Date | Não | Data de geração/alteração |
| CodUsu | Number(010,0) | Sim | Usuário geração/alteração |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- CodAcs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710SQA_005

**Tabela:** E710SQR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |
| SeqRot | SeqRot |
| SfxSeq | SfxSeq |

