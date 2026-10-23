# R583IMG

## Descrição

GHE - Revisão do GHE - Imagens

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| SeqImg | Number(003,0) | Não | Sequência da imagem |
| DesImg | String(050) | Sim | Descrição da imagem da revisão do GHE |
| Imagem | Image | Sim | Imagem da revisão do GHE |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583IMG_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

