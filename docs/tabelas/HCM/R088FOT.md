# R088FOT

## Descrição

Imagens do Veículo

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
| PlaVei | String(010) | Não | Placa do Veículo |
| SeqFot | Number(003,0) | Não | Código Foto |
| DesFot | String(030) | Sim | Descrição Foto |
| ImgVei | Image | Sim | Imagem Veículo |

---

## Chave Primária

- PlaVei
- SeqFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088FOT_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

