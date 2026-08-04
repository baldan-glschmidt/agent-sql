# E710IMG

## Descrição

Ficha - Roteiro - Imagem para Seqüência Operacional

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

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
| SeqImg | Number(004,0) | Não | Número seqüencial do detalhe (imagem) sobre a seqüência operacional |
| FotDet | String(014) | Não | Código da foto detalhe (imagem) técnico na seqüência operacional do processo |
| SeqFot | Number(004,0) | Não | Número seqüencial da foto no cadastro de fotos p/ operações |
| DatAlt | Date | Não | Data de geração/alteração |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710IMG_005

**Tabela:** E710SQR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |
| SeqRot | SeqRot |
| SfxSeq | SfxSeq |

### IR_E710IMG_008

**Tabela:** E720FOT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FotDet | FotDet |
| SeqFot | SeqFot |

