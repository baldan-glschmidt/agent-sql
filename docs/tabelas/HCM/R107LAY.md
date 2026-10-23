# R107LAY

## Descrição

Perfil PDI - Layout

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Código do perfil |
| GrpPDI | Number(002,0) | Não | Define o grupo de informações do layout |
| SeqGrd | Number(002,0) | Não | Sequência do grid de configuração |
| SeqCam | Number(003,0) | Não | Sequência do campo |
| TCpPDI | Number(001,0) | Sim | Tipo de campo - Texto estático / Campo de sistema |
| NomCam | String(040) | Sim | Nome do campo |
| RotCam | String(050) | Sim | Rótulo do campo |
| DicPre | String(250) | Sim | Dica de preenchimento |
| CamObr | Number(001,0) | Sim | Obrigatoriedade do campo |
| CamEdt | Number(001,0) | Sim | Editabilidade do campo |
| MosGri | Number(001,0) | Sim | Mostrar na grid |
| MosFor | Number(001,0) | Sim | Mostrar no formulário detalhe |
| NovLin | Number(001,0) | Sim | Define se deve apresentar a informação em uma nova linha |
| LarExi | Number(004,0) | Sim | Largura de exibição da informação |
| MosLnk | Number(001,0) | Sim | Define se a informação é exibida como Link |
| ValPad | String(8001) | Sim | Valor padrão |

---

## Chave Primária

- CodPer
- GrpPDI
- SeqGrd
- SeqCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107LAY_000

**Tabela:** R107PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

