# R510CSS

## Descrição

Currículo Web - Customização

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| CodCss | Number(002,0) | Não | Código da Customização |
| CamCss | String(101) | Sim | Caminho físico do arquivo para customização |
| TipArq | Number(001,0) | Sim | Tipo do arquivo para customização |

---

## Chave Primária

- CodPer
- CodCss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510CSS_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

