# R058PPT

## Descrição

Perspectivas de imagens dos modelos

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| PptImg | Number(001,0) | Não | Perspectiva da imagem do modelo |
| ImgMod | Image | Sim | Imagem do equipamento |

---

## Chave Primária

- ModRlg
- PptImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058PPT_000

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

