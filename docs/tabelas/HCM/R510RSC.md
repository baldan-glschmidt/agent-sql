# R510RSC

## Descrição

Currículo Web - Recuperação de Senha - Campos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRSP | Number(003,0) | Não | Código da política de recuperação de senha |
| CodCam | Number(004,0) | Não | Código do campo |
| SeqCam | Number(003,0) | Sim | Sequência do campo |
| TabBas | String(007) | Sim | Tabela-base |
| NomCam | String(040) | Sim | Nome do campo |
| RotCam | String(050) | Sim | Rótulo do campo |
| DicPre | String(250) | Sim | Dica de preenchimento |
| LarExi | Number(004,0) | Sim | Largura de exibição do campo |
| FilEnu | String(200) | Sim | abrangência dos valores exibidos na lista |

---

## Chave Primária

- CodRSP
- CodCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510RSC_000

**Tabela:** R510RSP

| Origem | Destino |
|--------|---------|
| CodRSP | CodRSP |

