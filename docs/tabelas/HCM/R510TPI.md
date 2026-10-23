# R510TPI

## Descrição

Termos de Uso e Privacidade Por Idioma

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodVer | Number(004,0) | Não | Código da Versão dos termos de uso e privacidade |
| IdiLay | Number(001,0) | Não | Idioma dos textos do termo de uso e privacidade |
| TexTer | String(50000) | Sim | Texto dos termos de uso e privacidade |
| TexRec | String(1000) | Sim | Mensagem de confirmação de recusa |
| TexAce | String(1000) | Sim | Mensagem de confirmação de aceite |

---

## Chave Primária

- CodVer
- IdiLay

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510TPI_000

**Tabela:** R510TUP

| Origem | Destino |
|--------|---------|
| CodVer | CodVer |

