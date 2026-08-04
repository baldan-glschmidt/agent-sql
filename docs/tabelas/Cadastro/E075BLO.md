# E075BLO

## Descrição

Cadastros - Produtos - Bloqueio

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqBlo | Number(009,0) | Não | Sequência do registro |
| SeqRpf | Number(009,0) | Não | Sequência do registro |
| CodDer | String(007) | Sim | Código da derivação |
| MotBlo | String(500) | Sim | Motivo do bloqueio |
| BloOrc | Number(001,0) | Sim | Indicativo de que deve bloquear o Orçamento |
| BloPed | Number(001,0) | Sim | Indicativo de que deve bloquear o Pedido |
| BloCtr | Number(001,0) | Sim | Indicativo de que deve bloquear o Contrato |
| BloPfa | Number(001,0) | Sim | Indicativo de que deve bloquear a Pré-Fatura |
| BloCar | Number(001,0) | Sim | Indicativo de que deve bloquear a Carga |
| BloNfv | Number(001,0) | Sim | Indicativo de que deve bloquear a Nota fiscal de saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- SeqBlo

---

## Índices

### E075BLOIndice1

**Tipo:** Não unico

Campos:
- SeqRpf
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
